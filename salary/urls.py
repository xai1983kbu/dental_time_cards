from django.urls import path

from . import views

app_name = 'salary'

urlpatterns = [
    path('', views.current_month, name='current_month'),
    path('another/<year>/<month>/', views.another_month, name='another_month'),
    path('edit/<year>/<month>/', views.edit, name='edit'),

    ]