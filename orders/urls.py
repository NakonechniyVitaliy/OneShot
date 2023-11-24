from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('bill', bill),
    path('ajax_cart', ajax_cart),
    path('ajax_cart_display', ajax_cart_display),
    path('order_delete', order_delete),
    path('order_delete_all', order_delete_all),
]
