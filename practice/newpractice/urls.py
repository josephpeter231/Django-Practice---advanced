from django.urls import path
from . import views

app_name = "newpractice"

urlpatterns=[
    path('app2/',views.home_view,name="home_view"),
    path('app2/about/',views.about_view,name="about_view")  
]

