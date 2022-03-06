from django.urls import path
from backend.views.product_views import *


urlpatterns = [
    path('', get_products, name='products'),
    path('<str:pk>/', get_product, name='product-detail'),
]
