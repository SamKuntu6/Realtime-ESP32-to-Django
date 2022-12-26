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

class BridgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'bridge_type', 'lanes_number', 'lane_width', 'ped_lane_width', 'effective_span', 'max_sema_deflection', 'location')

class InventoryDataAdmin(admin.ModelAdmin):
    list_display = ('main_activity', 'activities', 'status', 'cost', 'date')


admin.site.register(Data, DataAdmin)
admin.site.register(DayData, DayDataAdmin)
admin.site.register(MonthData, MonthDataAdmin)
admin.site.register(YearData, YearDataAdmin)
admin.site.register(Bridge, BridgeAdmin)
admin.site.register(InventoryData, InventoryDataAdmin)