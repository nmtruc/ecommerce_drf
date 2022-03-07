from django.urls import path
from backend.views.user_views import *


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', register_user, name='register'),
    path('profile/', get_user_profile, name='user-profile'),
    path('profile/update/', update_user_profile, name='user-profile'),
    path('', get_users, name='users'),
    path('<str:pk>/', get_user_by_id, name='get_user_by_id'),
    path('update/<str:pk>/', update_user, name='update_user'),
    path('delete/<str:pk>/', delete_user, name='delete_user'),
]
