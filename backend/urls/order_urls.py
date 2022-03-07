from django.urls import path
from backend.views.order_views import *


urlpatterns = [
    path('', get_orders, name='get_orders'),
    path('add/', add_order_items, name='add_order_items'),
    path('myorders/', get_my_orders, name='get_my_orders'),
    path('<str:pk>/deliver/', update_order_to_delivered,
         name='update_order_to_delivered'),
    path('<str:pk>/', get_order_by_id, name='get_order_by_id'),
    path('<str:pk>/pay/', update_order_to_paid, name='update_order_to_paid'),
]
