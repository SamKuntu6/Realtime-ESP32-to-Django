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
