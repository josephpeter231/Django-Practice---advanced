from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, home_view

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', home_view, name='home'),  
    path('', include(router.urls)),
]
