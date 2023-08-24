from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_products, name='products'),  # Add the 'name' parameter
    path('<int:venue_id>/', views.venue_detail, name='venue_detail'),
]