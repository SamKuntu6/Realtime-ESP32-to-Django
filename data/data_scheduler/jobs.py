from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
from data.models import *


def schedule_day_data():
    total = 0
    day_avg = 0
    dartime = datetime.now(pytz.timezone('Africa/Dar_es_Salaam'))
    day_items = Data.objects.filter(created__date=dartime.date())
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


def schedule_month_data():
    total = 0
    month_avg = 0
    dartime = datetime.now(pytz.timezone('Africa/Dar_es_Salaam'))

    # check if its january
    if dartime.month != 1:
        # month_items = DayData.objects.filter(created__month=(current_datetime.month-1))
        month_items = DayData.objects.filter(created__gte=dartime-relativedelta(months=1))
    else:
        month_items = DayData.objects.filter(created__month=dartime.month)

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
    dartime = datetime.now(pytz.timezone('Africa/Dar_es_Salaam'))
    year_items = MonthData.objects.filter(created__month=(dartime.year - 1))

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
