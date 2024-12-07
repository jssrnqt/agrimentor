from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import register_view, login_view

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]