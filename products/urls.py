from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:venue_id>/', views.venue_detail, name='venue_detail'),  # Make sure to use 'int:' to capture an integer value
    path('<int:product_id>/edit/', views.edit_product, name='edit_product'),  # Add this line for the edit URL
]
