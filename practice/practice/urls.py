# project/urls.py
from django.urls import path, include

urlpatterns = [
    path('main/', include('app1.urls', namespace='app_1')),  
    path('main2/', include('newpractice.urls', namespace='newpractice')),  
]
