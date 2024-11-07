# views.py
from django.http import HttpResponse
from django.urls import reverse

def home_view(request):
    about_url = reverse('about')  # Resolve URL for the 'about' view by its name
    response_content = f"<h1>Welcome to the Home Page</h1><p>Visit the <a href='{about_url}'>About Page</a></p>"
    return HttpResponse(response_content)

def about_view(request):
    home_url = reverse('home')  # Resolve URL for the 'home' view by its name
    response_content = f"<h1>About Us</h1><p>Go back to the <a href='{home_url}'>Home Page</a></p>"
    return HttpResponse(response_content)
