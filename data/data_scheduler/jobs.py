from django.conf import settings
import json
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import zoneinfo
from data.models import *
import math


def schedule_day_data():
    total = 0
    day_avg = 0
    dartime = zoneinfo.ZoneInfo("Africa/Dar_es_Salaam")
    today = date.today()
    day_items = Data.objects.filter(created__gte=today)
    if day_items:
        for item in day_items:
            total += item.strain

        day_avg = total / day_items.count()
    
    value = float(day_avg)
    value_float = round(value, 2)

    v_status = False
    v_cond = False

    if value_float >= 50:
        pass
    elif value_float >= 40 and value_float < 50:
        v_cond = True
    else:
        v_status = True

    DayData.objects.create(
        strain = value_float,
        created = dartime,
        condition = v_cond,
        status = v_status
    )
    print("Saving the day data ....!")


# def schedule_week_data():
#     week_items = DayData.objects.filter(created__gte=datetime.now()-timedelta(days=7))
#     print(week_items)
#     if week_items:
#         for items in week_items:
#             print(items.created.date())
#     print("data gani ....!")


def schedule_month_data():
    total = 0
    month_avg = 0
    dartime = zoneinfo.ZoneInfo("Africa/Dar_es_Salaam")
    current_datetime = datetime.now()

    # check if its january
    if current_datetime.month != 1:
        # month_items = DayData.objects.filter(created__month=(current_datetime.month-1))
        month_items = DayData.objects.filter(created__gte=datetime.now()-relativedelta(months=1))
    else:
        month_items = DayData.objects.filter(created__month=current_datetime.month)

    if month_items:
        for item in month_items:
            total += item.strain
            
        month_avg = total / month_items.count()

    value = float(month_avg)
    value_float = round(value, 2)

    v_status = False
    v_cond = False

    if value_float >= 50:
        pass
    elif value_float >= 40 and value_float < 50:
        v_cond = True
    else:
        v_status = True

    MonthData.objects.create(
        strain = value_float,
        created = dartime,
        condition = v_cond,
        status = v_status
    )
    print("Saving the month data ....!")


def schedule_year_data():
    total = 0
    year_avg = 0
    dartime = zoneinfo.ZoneInfo("Africa/Dar_es_Salaam")
    current_datetime = datetime.now()

    year_items = MonthData.objects.filter(created__month=(current_datetime.year - 1))

    if year_items:
        for item in year_items:
            total += item.strain

        year_avg = total / year_items.count()
    
    value = float(year_avg)
    value_float = round(value, 2)

    v_status = False
    v_cond = False

    if value_float >= 50:
        pass
    elif value_float >= 40 and value_float < 50:
        v_cond = True
    else:
        v_status = True

    YearData.objects.create(
        strain = value_float,
        created = dartime,
        condition = v_cond,
        status = v_status
    )
    print("Saving the year data ....!")
