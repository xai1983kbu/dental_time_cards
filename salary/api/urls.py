from django.urls import path

from salary.api.views import DaysAtWorkDetailView, DaysAtWorkAPIView


urlpatterns = [
    path('daysatwork/<id>/', DaysAtWorkDetailView.as_view(), name='detail'),
    path('daysatwork/', DaysAtWorkAPIView.as_view(), name='list')
]