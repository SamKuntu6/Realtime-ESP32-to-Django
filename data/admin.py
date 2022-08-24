from django.contrib import admin
from .models import *


class DataAdmin(admin.ModelAdmin):
    list_display = ('strain', 'updated', 'created')


admin.site.register(Data, DataAdmin)