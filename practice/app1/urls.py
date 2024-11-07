from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('app1/',views.testing,name='app_1')
]