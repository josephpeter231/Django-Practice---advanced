# urls.py
from django.urls import path,include
from app1 import views
urlpatterns = [
    path('main/',include('app1.urls',namespace = 'app1')),
    path('main2/',include('newpractice.urls',namespace='newpractice'))
]
