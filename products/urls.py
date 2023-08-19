from django.urls import path
from .  import views


urlpatterns = [
    path('', views.all_products, name='products'),
    path('<venue_id>', views.venue_detail, name='venue_detail'),
]
