from django.urls import path
from backend.views.product_views import *


urlpatterns = [
    path('', get_products, name='get_products'),
    path('create/', create_product, name='create_product'),
    path('upload/', upload_image, name='upload_image'),
    path('update/<str:pk>/', update_product, name='update_product'),
    path('delete/<str:pk>/', delete_product, name='delete_product'),
    path('<str:pk>/', get_product, name='get_product'),
]
