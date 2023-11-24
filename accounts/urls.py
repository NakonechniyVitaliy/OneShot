from django.urls import path
from .views import *

urlpatterns = [
    path('sign_in', sign_in),
    path('sign_out', sign_out),
    path('sign_up', sign_up),
    path('profile', profile)
]
