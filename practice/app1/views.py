from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def testing(request):
    return HttpResponse('app1 is working')