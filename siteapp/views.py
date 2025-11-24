from django.shortcuts import render
from .models import LandingPage

def home(request):
    page = LandingPage.objects.first()
    return render(request, "siteapp/home.html", {"page": page})
