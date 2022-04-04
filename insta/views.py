from django.shortcuts import render, redirect, get_object_or_404
from . models import Image
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
# /@login_required(login_url='/accounts/login')
def home(request):
    images= Image.get_images().order_by('-date_posted')
    return render(request, 'index.html', {'images': images})

def welcome(request):
    return HttpResponse("Welcome to instagram")
