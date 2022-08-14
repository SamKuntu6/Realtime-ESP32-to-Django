from . models import Data
from django.shortcuts import render, redirect
from django.http import JsonResponse
from user.decorators import unauthenticated_user


def get_strain_data(request, dataz=234):
    
    print(dataz)
    
    return redirect('data:homepage')


# @unauthenticated_user
def home_page(request):
    return render(request, 'data/home.html', {})


# @unauthenticated_user
def index_page(request):
    return render(request, 'data/index.html', {})


# @unauthenticated_user
def temperature_view(request):
    context = {}
    return render(request, 'data/temp.html', context)


# @unauthenticated_user
def err(request):
    return render(request, 'data/404.html', {})