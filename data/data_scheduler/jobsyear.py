from datetime import datetime
from dateutil.relativedelta import relativedelta
import pytz
from data.models import *


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
