from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('adjust_bag/<item_id>/', views.adjust_bag, name='adjust_bag'),  # Update this line
]

