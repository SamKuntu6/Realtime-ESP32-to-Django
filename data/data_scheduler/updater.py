from urllib import request
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .jobs import schedule_day_data, schedule_month_data, schedule_year_data


def start():
    scheduler = BackgroundScheduler()
    
    # making trials with intervaals of the scheduler
    # scheduler.add_job(job_day, 'interval', minutes=1, id="day_data001", replace_existing=True)

    scheduler.add_job(schedule_day_data, 'cron', day_of_week='0,1,2,3,4,5,6', hour='15', minute='16',
     second='1', id="day_data1", replace_existing=True)
    
    # Here saving the daily collection to DayData model
    # scheduler.add_job(schedule_week_data, 'cron', day_of_week='sun', hour='23', minute='59', 
    #  second='33', id="week_data2", replace_existing=True)

    # Here saving the monthly collection to MonthlyData model
    scheduler.add_job(schedule_month_data, 'cron', month= '1,2,3,4,5,6,7,8,9,10,11,12', day='1', 
     hour='0', minute='0', second='15', id="month_data3", replace_existing=True)
    
    # Here saving the yearly collection to YearlyData model
    scheduler.add_job(schedule_year_data, 'cron', month='1', day='1', hour='0', minute='5', 
     id="year_data4", replace_existing=True)

    scheduler.start()
