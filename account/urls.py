from django.urls import path
from .views import register_view, login_view, login_register, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('login_register/', login_register, name='login-register'),
    path('logout/', logout_view, name='logout'),
]
