from django.urls import path
from backend.views.product_views import *


urlpatterns = [
    path('', get_products, name='get_products'),
    path('create/', create_product, name='create_product'),
    path('upload/', upload_image, name='upload_image'),
    path('<str:pk>/reviews/', create_product_review,
         name='create_product_review'),
    path('top/', get_top_products, name='get_top_products'),
    path('<str:pk>/', get_product, name='get_product'),
    path('update/<str:pk>/', update_product, name='update_product'),
    path('delete/<str:pk>/', delete_product, name='delete_product'),
]
