from django.shortcuts import render
from rest_framework.response import Response
from decimal import Decimal
from rest_framework.decorators import api_view
from forecast.models import Weekly, Current_Weather, Rules
from datetime import datetime

def getstatus():
    status_temp =[0]
    rules = Rules.objects.all()
    first_weekly = Weekly.objects.filter(forecast_time__gte=datetime.now()).order_by('forecast_time').first()
    first_current = Current_Weather.objects.all().order_by('-current_time').first()
    #0-red 1-green 2-yellow 3-Manual
    for color in rules:
        flag=True
        for field in Rules._meta.get_fields():
            if field.name[0 : 3]=='min' :
                if(getattr(color,field.name)>getattr(first_current,field.name)):
                    flag=False
                    break
            elif field.name[0 : 3]=='max':
                if(getattr(color,field.name)<getattr(first_current,field.name)):
                    flag=False
                    break
            elif field.name=='weather':
                pass
        if flag:
            return color.status_type
    return "Green"







    if rules.exists() and rules.first().status_type == "Manual":
        return "Manual"
    if rules.exists():
        for rule in rules
    elif max(status_temp)==1:
        return "yellow"
    else:
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
