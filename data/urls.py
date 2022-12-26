from django.urls import path
from . import views 


app_name = 'data'

urlpatterns = [
    path('updatedata/<str:value>/',views.get_strain_data, name='api_data'),
    path('strain/', views.strain_page, name='strain_page'),
    path('index/', views.index_page, name='indexpage'),
    path('error/', views.err, name='error'),
    path('deflection', views.deck_defl, name='dec_dif'),
    path('bridge', views.bridge_info, name='bridge_info'),
    path('bridge/<str:val>/', views.one_bridge_info, name='one_bridge_info'),
    path('inventory', views.bridge_inve, name='bridge_inve'),
    path('importexcel', views.export_write_xls, name='export_write_xls'),
    path('daily_rep/', views.daily_rep, name='d_report'),
    path('weekly_rep/', views.weekly_rep, name='w_report'),
    path('monthly_rep/', views.monthly_rep, name='m_report'),
    path('yearly_rep/', views.yearly_rep, name='y_report'),
    path('temperature/',  views.displacement_view, name='temp_data')
]