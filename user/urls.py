from django.urls import path
from . import views 


app_name = 'user'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.sign_out, name='logout'),
]