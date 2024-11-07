from django.urls import path

from practice.app1.views import home_view
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('', home_view, name='home')
]
