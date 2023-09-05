from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),  # Add the 'name' parameter
    path('<int:venue_id>/', views.venue_detail, name='venue_detail'),
    path('products/<int:venue_id>/<str:booking_date>/', views.venue_detail, name='venue_detail'),

]

