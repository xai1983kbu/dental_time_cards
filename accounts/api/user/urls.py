from django.urls import path

from .views import UserDetailAPIView

urlpatterns = [
    path('<username>/', UserDetailAPIView.as_view(), name='detail'),
]