from .jobs import schedule_day_data, schedule_month_data, schedule_year_data
import pytz
from apscheduler.schedulers.background import BackgroundScheduler


def start():
  scheduler = BackgroundScheduler(timezone=pytz.timezone('Africa/Dar_es_Salaam'))
  
  scheduler.add_job(
    schedule_day_data, 'cron', day_of_week='0,1,2,3,4,5,6', hour='14', minute='03',second='10', 
    id="daydata",
    replace_existing=True
  )
  
  scheduler.add_job(
    schedule_month_data, 'cron', month= '1,2,3,4,5,6,7,8,9,10,11,12', day='26', hour='14', minute='03', second='25',
    id="monthdata",
    replace_existing=True
  )
  
  scheduler.add_job(
    schedule_year_data, 'cron', month='12', day='26', hour='14', minute='03',
    id="yeardata",
    replace_existing=True
  )
  
  try:
    scheduler.start()

  except (KeyboardInterrupt, SystemExit):
    scheduler.remove_job('daydata')
    scheduler.remove_job('monthdata')
    scheduler.remove_job('yeardata')

