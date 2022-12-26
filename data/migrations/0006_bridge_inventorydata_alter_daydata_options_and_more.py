# Generated by Django 4.1 on 2022-12-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_daydata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(default='Single Span Bridge', max_length=200)),
                ('lanes_number', models.IntegerField(blank=True, default='1', null=True)),
                ('lane_width', models.FloatField(blank=True, default=6.0, null=True)),
                ('ped_lane_width', models.FloatField(blank=True, default=1.0, null=True)),
                ('effective_span', models.FloatField(blank=True, default=100.0, null=True)),
                ('max_sema_deflection', models.FloatField(blank=True, default=1.0, null=True)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='InventoryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_activity', models.CharField(max_length=100)),
                ('activities', models.CharField(max_length=300)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('cost', models.CharField(max_length=20, null=True)),
                ('incharge', models.CharField(max_length=200, null=True)),
                ('date', models.CharField(max_length=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.AlterModelOptions(
            name='daydata',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='monthdata',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='yeardata',
            options={'ordering': ['-created']},
        ),
    ]
