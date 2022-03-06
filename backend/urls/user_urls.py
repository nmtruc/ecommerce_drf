from django.urls import path
from backend.views.user_views import *


urlpatterns = [
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('register/', register_user, name='register'),
    path('', get_users, name='users'),
    path('profile/', get_user_profile, name='user-profile'),
    path('profile/update/', update_user_profile, name='update-user-profile'),
]
