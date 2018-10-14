from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import AuthAPIView, RegisterAPIView
from accounts.api.user.views import curent_user

urlpatterns = [
    path('', AuthAPIView.as_view(), name='login_drf'),
    path('register/', RegisterAPIView.as_view(), name='register_drf'),
    path('jwt/', obtain_jwt_token),
    path('jwt/refresh/', refresh_jwt_token),
    path('curent_user/', curent_user)
]