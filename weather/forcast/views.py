from django.shortcuts import render
from .models import Weekly, Current_Weather

# Create your views here.
def status_view(request):
    """Status View
    Returns a badge with online status.

    Arguments:
        request {Requset} -- Request object.

    Returns:
        Response -- Response object.
    """

    weekly = Weekly.objects.all().order_by('-forcast_time')
    current_weather = Current_Weather.objects.all().order_by('-current_time')

    return activity
    context = {"weekly": weekly, "current_weather": current_weather}
    return render(request, 'dashboard.html', context)
