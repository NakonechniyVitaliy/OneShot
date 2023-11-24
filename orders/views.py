from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from orders.models import Order
from cloudipsp import Api, Checkout
from django.shortcuts import redirect
from django.core.mail import send_mail


def index(request):
    if request.method == 'GET':
        user_orders = Order.objects.filter(user_id=request.user.id)
        amount = 0
        for order in user_orders:
            amount += 1

        return render(request, 'orders/index.html', {
            'title': 'Кошик',
            'user_orders': Order.objects.filter(user_id=request.user.id),
            'amount': amount
    })

    elif request.method == 'POST':

        user_orders = Order.objects.filter(user_id=request.user.id)

        amount = 0
        for order in user_orders:
            amount += order.amount

        products = ''
        for order in user_orders:
            products += str(order.product) + ', '

        email = request.POST.get('email')

        subject = 'Message about ordering on the website SHOT'
        body = f'''
                <h1>{subject}</h1>
                <hr/>
                <h2 style="color: purple">
                    You have confirmed your order for the following products:
                </h2>
                <h2>{products}.</h2>
                <ol>
            '''
        body += f'''
                </ol>
                </h3>
                <hr/>
                <h2>
                    Amount to be paid:
                    <span style="color: red">
                        {amount}$ 
                    </span>
                </h2>
            '''
        success = send_mail(subject, '', 'shot-shop@gmail.com', [email], fail_silently=False, html_message=body)
        if success:
            return render(request, 'orders/thanks.html', {
                'title': 'Подяка за замовлення',
                'email': email
            })
        else:
            return render(request, 'orders/failed.html', {
            })


def bill(request):

    user_orders = Order.objects.filter(user_id=request.user.id)

    # Обчислюємо загальну вартість всіх замовлень даного користувача:
    amount = 0
    for order in user_orders:
        amount += order.amount

    api = Api(merchant_id=1396424,
              secret_key='test')
    checkout = Checkout(api=api)
    data = {
        "currency": "USD",
        "amount": str(amount) + "00"
    }
    url = checkout.url(data).get('checkout_url')
    return redirect(url)


def ajax_cart(request):
    response = dict()
    response['message'] = 'Привіт від сервера!'

    # 1 - Отримуємо значення GET-параметрів від клієнта:
    uid = request.GET.get('uid')
    pid = request.GET.get('pid')
    price = request.GET.get('price')

    # 2 - Створюємо нове замовлення та зберігаємо його в БД:
    Order.objects.create(
        title=f'Order-{pid}/{uid}/{timezone.now()}',
        user_id=uid,
        product_id=pid,
        amount=float(price),
        notes='Очікує підтвердження'
    )

    # 3 - Зчитуємо із бази список всіх замовлень даного користувача:
    user_orders = Order.objects.filter(user_id=uid)

    # 4 - Обчислюємо загальну вартість всіх замовлень даного користувача:
    amount = 0
    for order in user_orders:
        amount += order.amount

    # 5 - Записуємо у відповідь сервера загальну вартість та кількість товарів:
    response['amount'] = amount
    response['count'] = len(user_orders)

    return JsonResponse(response)


def ajax_cart_display(request):
    # 1
    response = dict()
    response['message'] = 'AJAX-cart_display-OK'

    # 2
    uid = request.GET.get('uid')
    response['uid'] = uid

    # 3
    user_products = Order.objects.filter(user_id=uid)
    amount = 0

    # 4
    for product in user_products:
        amount += product.amount

    # 5
    response['count'] = len(user_products)
    response['total'] = amount

    return JsonResponse(response)


def order_delete(request):
    response = dict()

    oid = request.GET.get('oid')
    uid = request.GET.get('uid')

    Order.objects.filter(id=oid).delete()


def order_delete_all(request):
    response = dict()

    oid = request.GET.get('oid')
    uid = request.GET.get('uid')
    user_orders = Order.objects.filter(user_id=uid)
    user_orders.delete()