from django.shortcuts import render
from .models import Service

# Create your views here.
def index(request):
    service=Service.objects.all()
    return render(request,'index.html',{'service':service})
def project(request):
    return render(request,'project.html')
def privacy(request):
    return render(request,'privacy.html')
def terms(request):
    return render(request,'terms.html')