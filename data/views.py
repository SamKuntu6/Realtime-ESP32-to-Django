from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import *
from datetime import datetime, timedelta, date
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from user.decorators import unauthenticated_user
from .serializer import DataSerializer
from django.db.models import Count, Sum
import zoneinfo
from . import documentor
import io


@api_view(['GET'])
def get_strain_data(request, value):
    data_v = request.data
    # current_datetime = datetime.now()
    dartime = zoneinfo.ZoneInfo("Africa/Dar_es_Salaam")
    value_float = float(value)

    v_status = False
    v_cond = False

    if value_float >= 50:
        pass
    elif value_float >= 40 and value_float < 50:
        v_cond = True
    else:
        v_status = True

    data_value = Data.objects.create(
        strain = value_float,
        created = dartime,
        condition = v_cond,
        status = v_status
    )

    serializer = DataSerializer(data_value, many=False)
    print(data_value)
    return Response(serializer.data)


@login_required(login_url='user:login')
def strain_page(request):
    strain_value = "kituuuu"
    print("inside strain page")
    return render(request, 'data/strain.html', {'strain': strain_value})


@login_required(login_url='user:login')
def index_page(request):
    return render(request, 'data/index.html', {})


@login_required(login_url='user:login')
def displacement_view(request):
    context = {}
    return render(request, 'data/temp.html', context)


@login_required(login_url='user:login')
def err(request):
    return render(request, 'data/404.html', {})


@login_required(login_url='user:login')
def deck_defl(request):
    if request.method == 'POST' and (request.POST.get('interval')) is not None:
        selected = int(request.POST.get('interval'))
        if selected == 1:
            today = date.today()
            day_datas = Data.objects.filter(created__gte=today)
            checker = 'day'
            heading = "Today's"
            print(f'It is a day request {today}......{day_datas}')
            return render(request, 'data/deck_deflection.html', {'disp_items':day_datas, 'interval':checker, 'head':heading})
        elif selected == 2:
            week_datas = DayData.objects.filter(created__gte=datetime.now()-timedelta(days=7))
            checker = 'week'
            heading = "Last Seven Days'"
            print(f'It is a weeks data request {datetime.now()}......{week_datas}')
            return render(request, 'data/deck_deflection.html', {'disp_items':week_datas, 'interval':checker, 'head':heading})
        elif selected == 3:
            current_datetime = datetime.now()
            month_datas = MonthData.objects.all()
            checker = 'month'
            heading = "Months"
            print(f'It is a month data request {current_datetime.month}......{month_datas}')
            return render(request, 'data/deck_deflection.html', {'disp_items':month_datas, 'interval':checker, 'head':heading})
        elif selected == 4:
            current_datetime = datetime.now()
            year_datas = YearData.objects.all()
            checker = 'year'
            heading = "Year"
            print(f'It is a year data request {current_datetime.year}......{year_datas}')
            return render(request, 'data/deck_deflection.html', {'disp_items':year_datas, 'interval':checker, 'head':heading})
        else:
            today = date.today()
            day_datas = Data.objects.filter(created__gte=today)
            return render(request, 'data/deck_deflection.html', {'disp_items':day_datas, 'interval':checker})
    else:
        return render(request, 'data/deck_deflection.html', {})


@login_required(login_url='user:login')
def daily_rep(request):
    #Getting data needed after submit the form in the page
    now_time = datetime.now()
    time1 = now_time.ctime()  # get curent time
    if int(now_time.day) == 1:
        if int(now_time.month) == 1:
            time2 = f'Last Day of Last Year  ( 00:00 - 23:59 )' # Tabulation Time
        else:
            time2 = f'{now_time.year}-{now_time.month-1}- Previous Day  ( 00:00 - 23:59 )' # Tabulation Time
    else:
        time2 = f'{now_time.year}-{now_time.month}-{now_time.day-1}  ( 00:00 - 23:59 )' # Tabulation Time

    checker = 'Daily'
    
    rec = DayData.objects.last()
    if rec:
        record = rec.strain
        if record.strain >= 50:
            state = 'Working is Good'
            readings = True
        elif record.strain >= 40 and record.strain <= 50:
            state = 'Working Moderately Fine.'
            readings = True
        else:
            state = 'Working Conditions Dangerous.'
            readings = False
    else:
        state = 'Not yet recorded (Working Fine)'
        readings = True

    #Report creation
    word_doc = documentor.word_creator(checker, time1, time2, state, readings) 
    doc_io = io.BytesIO()
    word_doc.save(doc_io)  # save to memory stream
    doc_io.seek(0)

    # rewind the stream
    response = HttpResponse(
    doc_io.getvalue(),
    content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

    response["Content-Disposition"] = 'attachment; filename = "Daily_Report_({now_time.date}).docx"'
    response["Content-Encoding"] = "UTF-8"
    return response


@login_required(login_url='user:login')
def weekly_rep(request):
    #Getting data needed after submit the form in the page
    now_time = datetime.now()
    time1 = now_time.ctime()  # get curent time
    
    time2 = f'Last Seven Days Average  ( 00:00 - 23:59 )' # Tabulation Time

    checker = 'Weekly'

    week_items = DayData.objects.filter(created__gte=datetime.now()-timedelta(days=7))
    total = 0
    if week_items:
        for item in week_items:
            total += item.strain
        record = total / week_items.count()
    
        if record >= 50:
            state = 'Working is Good'
            readings = True
        elif record >= 40 and record <= 50:
            state = 'Working Moderately Fine.'
            readings = True
        else:
            state = 'Working Conditions Dangerous'
            readings = False
    else:
        state = 'Not yet recorded {Working Fine}'
        readings = True

    #Report creation
    word_doc = documentor.word_creator(checker, time1, time2, state, readings) 
    doc_io = io.BytesIO()
    word_doc.save(doc_io)  # save to memory stream
    doc_io.seek(0)

    # rewind the stream
    response = HttpResponse(
    doc_io.getvalue(),
    content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

    response["Content-Disposition"] = 'attachment; filename = "Weekly_Report.docx"'
    response["Content-Encoding"] = "UTF-8"
    return response


@login_required(login_url='user:login')
def monthly_rep(request):
    #Getting data needed after submit the form in the page
    now_time = datetime.now()
    time1 = now_time.ctime()  # get curent time
    
    if int(now_time.month) == 1:
        time2 = f'{now_time.year - 1} - December   ( Ist - 31st December)' # Tabulation Time
    else:
        time2 = f'{now_time.year} - {now_time.month-1}   ( Average Data Monthly )' # Tabulation Time

    checker = 'Monthly'

    month_item = MonthData.objects.last()
    if month_item:
        record = month_item.strain
        if record >= 50:
            state = 'Working is Good'
            readings = True
        elif record >= 40 and record <= 50:
            state = 'Working Moderately Fine.'
            readings = True
        else:
            state = 'Working Conditions Dangerous'
            readings = False
    else:
        state = 'Not yet recorded {Working Fine}'
        readings = True

    #Report creation
    word_doc = documentor.word_creator(checker, time1, time2, state, readings) 
    doc_io = io.BytesIO()
    word_doc.save(doc_io)  # save to memory stream
    doc_io.seek(0)

    # rewind the stream
    response = HttpResponse(
    doc_io.getvalue(),
    content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

    response["Content-Disposition"] = 'attachment; filename = "Monthly_Report.docx"'
    response["Content-Encoding"] = "UTF-8"
    return response


@login_required(login_url='user:login')
def yearly_rep(request):
    #Getting data needed after submit the form in the page
    now_time = datetime.now()
    time1 = now_time.ctime()  #get curent time
        
    time2 = f'{now_time.year-1}   ( Prevoius Year )'  #Tabulation Time

    checker = 'Yearly'

    year_item = YearData.objects.last()
    if year_item:
        record = year_item.strain
        if record >= 50:
            state = 'Working is Good'
            readings = True
        elif record >= 40 and record <= 50:
            state = 'Working Moderately Fine.'
            readings = True
        else:
            state = 'Working Conditions Dangerous'
            readings = False
    else:
        state = 'Not yet recorded {Working Fine}'
        readings = True

    #Report creation
    word_doc = documentor.word_creator(checker, time1, time2, state, readings) 
    doc_io = io.BytesIO()
    word_doc.save(doc_io)  # save to memory stream
    doc_io.seek(0)

    # rewind the stream
    response = HttpResponse(
    doc_io.getvalue(),
    content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )

    response["Content-Disposition"] = 'attachment; filename = "Yearly_Report.docx"'
    response["Content-Encoding"] = "UTF-8"
    return response
