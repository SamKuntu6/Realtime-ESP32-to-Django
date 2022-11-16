from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user


@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username_usr = request.POST.get('username')
        password_val = request.POST.get('password')
        
        user = authenticate(request, username=username_usr, password=password_val)
        if user is not None:
            login(request, user)
            request.session['user'] = username_usr
            return redirect('data:indexpage')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'user/login.html', context)


@login_required(login_url='user:login')
def sign_out(request):
    try:
        logout(request)
        del request.session['user']
    except:
        return redirect('user:login')
    
    return redirect('user:login')


def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        context = {'current_user': current_user}
        return render(request, 'data/index.html', context)
    else:
        return render(request, 'user/home.html', {})
