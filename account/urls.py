from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Авторизация
    # path('login/', views.user_login, name='login'),

    # Авторизация
    path('', views.dashboard, name='dashboard'),
]
