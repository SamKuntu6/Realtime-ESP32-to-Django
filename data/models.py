from django.db import models


class Data(models.Model):
    strain = models.FloatField()
    status = models.BooleanField(default=False)
    condition = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{:.2f}".format(self.strain)

    class Meta:
        ordering = ['-created']


class DayData(models.Model):
    strain = models.FloatField()
    status = models.BooleanField(default=False)
    condition = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{:.2f}".format(self.strain)

    class Meta:
        ordering = ['-created']


class MonthData(models.Model):
    strain = models.FloatField()
    status = models.BooleanField(default=False)
    condition = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{:.2f}".format(self.strain)

    class Meta:
        ordering = ['-created']


class YearData(models.Model):
    strain = models.FloatField()
    status = models.BooleanField(default=False)
    condition = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{:.2f}".format(self.strain)

    class Meta:
        ordering = ['-created']


class Bridge(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    bridge_type = models.CharField(max_length=200, default='Single Span Bridge')
    lanes_number = models.IntegerField(default='1', null=True, blank=True)
    lane_width = models.FloatField(default=6.0, null=True, blank=True)
    ped_lane_width = models.FloatField(default=1.0, null=True, blank=True)
    effective_span = models.FloatField(default=100.0, null=True, blank=True)
    max_sema_deflection = models.FloatField(default=1.0, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    class Meta:
        ordering = ['-created']


class InventoryData(models.Model):
    main_activity = models.CharField(max_length=100)
    activities = models.CharField(max_length=300)
    status = models.CharField(max_length=20, null=True, blank=True)
    cost = models.CharField(max_length=20, null=True)
    date = models.CharField(max_length=100, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.main_activity}'

    class Meta:
        ordering = ['-created']