from django.shortcuts import render
from .models import personalport
# Create your views here.
def home(request):
    projects = personalport.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
