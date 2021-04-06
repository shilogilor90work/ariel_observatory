from django.shortcuts import render
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
        Response -- Response object.
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
        Response -- Response object.
    """
    rules = Rules.objects.all()
    context = {"rules": rules}
    return render(request, 'rules.html', context)


@api_view(['POST'])
def hello_world(request):
    """Hello World"""
    return Response({"message": "Hello, world!"})
