from django.contrib import admin
from .models import *


class DataAdmin(admin.ModelAdmin):
    list_display = ('strain', 'updated', 'created')

class DayDataAdmin(admin.ModelAdmin):
    list_display = ('strain', 'updated', 'created')

class MonthDataAdmin(admin.ModelAdmin):
    list_display = ('strain', 'updated', 'created')

class YearDataAdmin(admin.ModelAdmin):
    list_display = ('strain', 'updated', 'created')


admin.site.register(Data, DataAdmin)
admin.site.register(DayData, DayDataAdmin)
admin.site.register(MonthData, MonthDataAdmin)
admin.site.register(YearData, YearDataAdmin)