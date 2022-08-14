from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('data.urls', namespace='data')),
    path('', include('user.urls', namespace='user')),
]
