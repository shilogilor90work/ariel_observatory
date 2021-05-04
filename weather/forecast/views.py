from django.shortcuts import render
from rest_framework.response import Response
from decimal import Decimal
from rest_framework.decorators import api_view
from forecast.models import Weekly, Current_Weather, Rules
from datetime import datetime

def getstatus():
    status_temp
    rule = Rules.objects.all()
    first_weekly = Weekly.objects.filter(forecast_time__gte=datetime.now()).order_by('forecast_time')
     if rule.exists() and rule.first().status_type == "Manual":
         return "Manual"
    if rule.exists():
        if rule.min_rain<5
            status_temp.append(0)
        elif rule.min_rain<10
            status_temp.append(1)
        else
            return "red"
        if rule.max_rain<5
            status_temp.append(0)
        elif rule.max_rain<10
            status_temp.append(1)
        else
            return "red"
        if rule.min_wsmax<5
            status_temp.append(0)
        elif rule.min_wsmax<10
            status_temp.append(1)
        else
            return "red"
        if rule.max_wsmax<5
            status_temp.append(0)
        elif rule.max_wsmax<10
            status_temp.append(1)
        else
            return "red"
        if rule.min_wdmax<5
            status_temp.append(0)
        elif rule.min_wdmax<10
            status_temp.append(1)
        else
            return "red"
        if rule.max_wdmax<5
            status_temp.append(0)
        elif rule.max_wdmax<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_ws<5
            status_temp.append(0)
        elif rule.min_ws<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_ws<5
            status_temp.append(0)
        elif rule.max_ws<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_wd<5
            status_temp.append(0)
        elif rule.min_wd<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_wd<5
            status_temp.append(0)
        elif rule.max_wd<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_stdwd<5
            status_temp.append(0)
        elif rule.min_stdwd<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_stdwd<5
            status_temp.append(0)
        elif rule.max_stdwd<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_td<5
            status_temp.append(0)
        elif rule.min_td<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_td<5
            status_temp.append(0)
        elif rule.max_td<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_td<5
            status_temp.append(0)
        elif rule.min_td<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_td<5
            status_temp.append(0)
        elif rule.max_td<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_tw<5
            status_temp.append(0)
        elif rule.min_tw<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_tw<5
            status_temp.append(0)
        elif rule.max_tw<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_tdmax<5
            status_temp.append(0)
        elif rule.min_tdmax<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_tdmax<5
            status_temp.append(0)
        elif rule.max_tdmax<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_tdmin<5
            status_temp.append(0)
        elif rule.min_tdmin<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_tdmin<5
            status_temp.append(0)
        elif rule.max_tdmin<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_ws1mm<5
            status_temp.append(0)
        elif rule.min_ws1mm<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_ws1mm<5
            status_temp.append(0)
        elif rule.max_ws1mm<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_ws10mm<5
            status_temp.append(0)
        elif rule.min_ws10mm<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_ws10mm<5
            status_temp.append(0)
        elif rule.max_ws10mm<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_time<5
            status_temp.append(0)
        elif rule.min_time<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_time<5
            status_temp.append(0)
        elif rule.max_time<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_tg<5
            status_temp.append(0)
        elif rule.min_tg<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_tg<5
            status_temp.append(0)
        elif rule.max_tg<10
            status_temp.append(1)
        else
            return "red"

        if rule.min_rh<5
            status_temp.append(0)
        elif rule.min_rh<10
            status_temp.append(1)
        else
            return "red"

        if rule.max_rh<5
            status_temp.append(0)
        elif rule.max_rh<10
            status_temp.append(1)
        else
            return "red"

        if rule.weather<5
            status_temp.append(0)
        elif rule.weather<10
            status_temp.append(1)
        else
            return "red"



    elif status_temp.max()==1
        return "yellow"
    else
        return "green"

# Create your views here.
def status_view(request):
    """Status View
    Returns a page with online status.

    Arguments:
        request {Requset} -- Request object.

    Returns:
        Render -- Render object.
    """
    status=getstatus()
    weekly = Weekly.objects.all().order_by('-forecast_time')
    current_weather = Current_Weather.objects.all().order_by('-current_time')
    context = {"weekly": weekly, "current_weather": current_weather, "status": status}
    return render(request, 'dashboard.html', context)


def rules_view(request):
    """Rules View
    Returns a page with online status rules.

    Arguments:
        request {Requset} -- Request object.

    Returns:
        Render -- Render object.
    """
    status=getstatus()
    rules = Rules.objects.all()
    context = {"rules": rules, "status": status}
    return render(request, 'rules.html', context)


@api_view(['POST'])
def hello_world(request):
    """Hello World"""
    print(request)
    return render(request, 'dashboard.html', context)
    # return Response({"message": "Hello, world!"})


@api_view(['POST'])
def update_rules(request):
    """Update Rules
    updates the database with the new rules and returns the status
        Arguments:
            request {Requset} -- Request object.

        Returns:
            Response -- Response object.
    """
    print(request)
    rule = Rules.objects.filter(status_type=request.POST.get('status_type'))
    if rule.exists() and rule.first().status_type == "Manual":
        print("Manual")
    elif rule.exists():
        rule = rule.first()
        rule.min_rain = Decimal(request.POST.get('min_rain'))
        rule.max_rain = Decimal(request.POST.get('max_rain'))
        rule.min_wsmax = Decimal(request.POST.get('min_wsmax'))
        rule.max_wsmax = Decimal(request.POST.get('max_wsmax'))
        rule.min_wdmax = Decimal(request.POST.get('min_wdmax'))
        rule.max_wdmax = Decimal(request.POST.get('max_wdmax'))
        rule.min_ws = Decimal(request.POST.get('min_ws'))
        rule.max_ws = Decimal(request.POST.get('max_ws'))
        rule.min_wd = Decimal(request.POST.get('min_wd'))
        rule.max_wd = Decimal(request.POST.get('max_wd'))
        rule.min_stdwd = Decimal(request.POST.get('min_stdwd'))
        rule.max_stdwd = Decimal(request.POST.get('max_stdwd'))
        rule.min_td = Decimal(request.POST.get('min_td'))
        rule.max_td = Decimal(request.POST.get('max_td'))
        rule.min_tw = Decimal(request.POST.get('min_tw'))
        rule.max_tw = Decimal(request.POST.get('max_tw'))
        rule.min_tdmax = Decimal(request.POST.get('min_tdmax'))
        rule.max_tdmax = Decimal(request.POST.get('max_tdmax'))
        rule.min_tdmin = Decimal(request.POST.get('min_tdmin'))
        rule.max_tdmin = Decimal(request.POST.get('max_tdmin'))
        rule.min_ws1mm = Decimal(request.POST.get('min_ws1mm'))
        rule.max_ws1mm = Decimal(request.POST.get('max_ws1mm'))
        rule.min_ws10mm = Decimal(request.POST.get('min_ws10mm'))
        rule.max_ws10mm = Decimal(request.POST.get('max_ws10mm'))
        rule.min_time = Decimal(request.POST.get('min_time'))
        rule.max_time = Decimal(request.POST.get('max_time'))
        rule.min_tg = Decimal(request.POST.get('min_tg'))
        rule.max_tg = Decimal(request.POST.get('max_tg'))
        rule.min_rh = Decimal(request.POST.get('min_rh'))
        rule.max_rh = Decimal(request.POST.get('max_rh'))
        rule.weather = request.POST.get('weather')
        rule.save()

    return Response({"message": str(request.POST.get('status_type')) + " was updated"})
