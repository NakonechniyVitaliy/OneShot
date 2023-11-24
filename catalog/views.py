from django.shortcuts import render
from .models import *
from orders.models import Order
from django.core.paginator import Paginator
from django.shortcuts import render, redirect


def index(request):
    transit_data = dict()
    transit_data['title'] = 'Каталог'

    all_products = Product.objects.all()
    transit_data['all_products'] = all_products

    all_category = Category.objects.all()
    transit_data['all_categories'] = all_category

    all_producer = Producer.objects.all()
    transit_data['all_producers'] = all_producer

    all_orders = Order.objects.filter(user_id=request.user.id)
    transit_data['user_orders'] = all_orders                                            # Відображення кошика 
    transit_data['user_orders']: Order.objects.filter(user_id=request.user.id)

    products_count = len(all_products)  # Рахуємо кількість об'ектів у кожній моделі
    producer_count = len(all_producer)
    category_count = len(all_category)

    transit_data['products_count'] = len(all_products)
    transit_data['producer_count'] = len(all_producer)
    transit_data['category_count'] = len(all_category)

    paginator = Paginator(all_products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    transit_data['page_obj'] = page_obj

    return render(request, 'catalog/index.html', context=transit_data)


def detail(request, product_id):
    transit_data = dict()
    transit_data['user_orders']: Order.objects.filter(user_id=request.user.id)

    all_orders = Order.objects.filter(user_id=request.user.id)
    transit_data['user_orders'] = all_orders
    transit_data['user_orders']: Order.objects.filter(user_id=request.user.id)

    target_product = Product.objects.get(id=product_id)
    target_product_double_price = target_product.price + 37.0
    if request.method == 'GET':
        transit_data['target_product'] = target_product
        transit_data['target_product_double_price'] = target_product_double_price
        return render(request, 'catalog/detail.html', context=transit_data)
    elif request.method == 'POST':
        return redirect('/catalog/index')