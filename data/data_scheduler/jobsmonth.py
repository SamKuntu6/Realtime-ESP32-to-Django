from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
from data.models import *


def schedule_month_data():
    total = 0
    month_avg = 0
    dartime = datetime.now(pytz.timezone('Africa/Dar_es_Salaam'))

    # check if its january
    if dartime.month != 1:
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
