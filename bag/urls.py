from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),  # Add a comma here
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),  # Corrected the period to a comma
]

