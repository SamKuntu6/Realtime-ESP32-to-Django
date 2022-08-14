from django.urls import path
from . import views 


app_name = 'data'

urlpatterns = [
    path('',views.get_strain_data, name='home'),
    path('home/', views.home_page, name='homepage'),
    path('index/', views.index_page, name='indexpage'),
    path('error/', views.err, name='error'),
    path('temp/',  views.temperature_view, name='temp')
]