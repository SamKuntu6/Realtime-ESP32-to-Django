from django.urls import path
from . import views 


app_name = 'data'

urlpatterns = [
    path('updatedata/<str:value>/',views.get_strain_data, name='api_data'),
    path('strain/', views.strain_page, name='strain_page'),
    path('index/', views.index_page, name='indexpage'),
    path('error/', views.err, name='error'),
    path('displacement/',  views.displacement_view, name='displacement_data')
]
