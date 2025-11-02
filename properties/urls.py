from django.urls import path
from . import views

urlpatterns = [
    # المسار /properties/ سيعرض view الـ property_list
    path('', views.property_list, name='property_list'),
]