from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import Data
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from user.decorators import unauthenticated_user
from .serializer import DataSerializer


@api_view(['GET'])
def get_strain_data(request, value):
    data_v = request.data
    value_float = float(value)

    data_value = Data.objects.create(
        strain = value_float
    )

    serializer = DataSerializer(data_value, many=False)
    
    print(data_value)
    return Response(serializer.data)


@login_required(login_url='user:login')
def strain_page(request):
    return render(request, 'data/strain.html', {})


@login_required(login_url='user:login')
def index_page(request):
    return render(request, 'data/index.html', {})


@login_required(login_url='user:login')
def displacement_view(request):
    context = {}
    return render(request, 'data/temp.html', context)


@login_required(login_url='user:login')
def err(request):
    return render(request, 'data/404.html', {})
