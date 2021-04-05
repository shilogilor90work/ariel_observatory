from django.shortcuts import render
from forecast.models import Weekly, Current_Weather
def getstatus():
    return "red"
# Create your views here.
def status_view(request):
    """Status View
    Returns a badge with online status.

    Arguments:
        request {Requset} -- Request object.

    Returns:
        Response -- Response object.
    """
    status=getstatus()
    weekly = Weekly.objects.all().order_by('-forecast_time')
    current_weather = Current_Weather.objects.all().order_by('-current_time')
    context = {"weekly": weekly, "current_weather": current_weather, "status": status}
    return render(request, 'dashboard.html', context)
