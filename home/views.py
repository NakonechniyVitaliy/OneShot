from django.shortcuts import render
from orders.models import Order


def index(request):
    return render(request, 'home/index.html', {
        'title': 'Головна',
        'page': 'index',
        'app': 'home',
        'user_orders': Order.objects.filter(user_id=request.user.id),
    })


def about(request):
    return render(request, 'home/about.html', {
        'title': 'Про сайт',
        'page': 'about',
        'app': 'home'
    })


def contacts(request):
    return render(request, 'home/contacts.html', {
        'title': 'Контакти',
        'page': 'contacts',
        'app': 'home'
    })

