from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:venue_id>/', views.venue_detail, name='venue_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:venue_id>/', views.edit_product, name='edit_product'),
]
