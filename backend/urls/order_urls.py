from django.urls import path
from backend.views.order_views import *


urlpatterns = [
    path('add/', add_order_items, name='add_order_items'),
]
