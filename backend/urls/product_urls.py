from django.urls import path
from backend.views.product_views import *


urlpatterns = [
    path('', get_products, name='get_products'),
    path('<str:pk>/', get_product, name='get_product'),
    path('delete/<str:pk>/', delete_product, name='delete_product'),
]
