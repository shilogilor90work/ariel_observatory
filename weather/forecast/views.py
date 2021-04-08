from django.shortcuts import render
from rest_framework.response import Response
from decimal import Decimal
from rest_framework.decorators import api_view
from forecast.models import Weekly, Current_Weather, Rules


def getstatus():
    return "red"

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
    rules = Rules.objects.all()
    context = {"rules": rules}
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
    if rule.exists() and rule.status_type == "Manual":
        print("Manual")
    elif rule.exists():
        rule.update(min_rain=50.5)

        # rule.update(min_rain=Decimal(request.POST.get('min_rain')), max_rain=Decimal(request.POST.get('max_rain')), min_wsmax=Decimal(request.POST.get('min_wsmax')), max_wsmax=Decimal(request.POST.get('max_wsmax')),
    #     min_wdmax=Decimal(request.POST.get('min_wdmax')), max_wdmax=Decimal(request.POST.get('max_wdmax')), min_ws=Decimal(request.POST.get('min_ws')), max_ws=Decimal(request.POST.get('max_ws')), min_wd=Decimal(request.POST.get('min_wd')),
    #     max_wd=Decimal(request.POST.get('max_wd')), min_stdwd=Decimal(request.POST.get('min_stdwd')),
    #     max_stdwd=Decimal(request.POST.get('max_stdwd')), min_td=Decimal(request.POST.get('min_td')), max_td=Decimal(request.POST.get('max_td')), min_tw=Decimal(request.POST.get('min_tw')),
    #     max_tw=Decimal(request.POST.get('max_tw')), min_tdmax=Decimal(request.POST.get('min_tdmax')), max_tdmax=Decimal(request.POST.get('max_tdmax')), min_tdmin=Decimal(request.POST.get('min_tdmin')), max_tdmin=Decimal(request.POST.get('max_tdmin')),
    #     min_ws1mm=Decimal(request.POST.get('min_ws1mm')), max_ws1mm=Decimal(request.POST.get('max_ws1mm')), min_ws10mm=Decimal(request.POST.get('min_ws10mm')), max_ws10mm=Decimal(request.POST.get('max_ws10mm')),
    #     min_time=Decimal(request.POST.get('min_time')), max_time=Decimal(request.POST.get('max_time')), min_tg=Decimal(request.POST.get('min_tg')), max_tg=Decimal(request.POST.get('max_tg')),
    #     min_rh=Decimal(request.POST.get('min_rh')), max_rh=Decimal(request.POST.get('max_rh')), weather=str(request.POST.get('weather')))
    # else:
    #     Rules.objects.create(status_type=request.POST.get('status_type'), min_rain=Decimal(request.POST.get('min_rain')), max_rain=Decimal(request.POST.get('max_rain')), min_wsmax=Decimal(request.POST.get('min_wsmax')), max_wsmax=Decimal(request.POST.get('max_wsmax')),
    #     min_wdmax=Decimal(request.POST.get('min_wdmax')), max_wdmax=Decimal(request.POST.get('max_wdmax')), min_ws=Decimal(request.POST.get('min_ws')), max_ws=Decimal(request.POST.get('max_ws')), min_wd=Decimal(request.POST.get('min_wd')),
    #     max_wd=Decimal(request.POST.get('max_wd')), min_stdwd=Decimal(request.POST.get('min_stdwd')),
    #     max_stdwd=Decimal(request.POST.get('max_stdwd')), min_td=Decimal(request.POST.get('min_td')), max_td=Decimal(request.POST.get('max_td')), min_tw=Decimal(request.POST.get('min_tw')),
    #     max_tw=Decimal(request.POST.get('max_tw')), min_tdmax=Decimal(request.POST.get('min_tdmax')), max_tdmax=Decimal(request.POST.get('max_tdmax')), min_tdmin=Decimal(request.POST.get('min_tdmin')), max_tdmin=Decimal(request.POST.get('max_tdmin')),
    #     min_ws1mm=Decimal(request.POST.get('min_ws1mm')), max_ws1mm=Decimal(request.POST.get('max_ws1mm')), min_ws10mm=Decimal(request.POST.get('min_ws10mm')), max_ws10mm=Decimal(request.POST.get('max_ws10mm')),
    #     min_time=Decimal(request.POST.get('min_time')), max_time=Decimal(request.POST.get('max_time')), min_tg=Decimal(request.POST.get('min_tg')), max_tg=Decimal(request.POST.get('max_tg')),
        # min_rh=Decimal(request.POST.get('min_rh')), max_rh=Decimal(request.POST.get('max_rh')), weather=str(request.POST.get('weather')))
    # return render(request, 'dashboard.html', context)
    return Response({"message": request.POST.get('status_type')})
