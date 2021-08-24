
from django.urls import path
from . import views


urlpatterns = [
    path('',  views.status_view, name="dashboard"),
    path('api_status/ariel',  views.api_status, name="api_status"),
    path('api_current/ariel',  views.api_current, name="api_current"),
    path('rules/',  views.rules_view, name="rules"),
    path('rules/hello_world/',  views.hello_world, name="hello_world"),
    path('rules/update_rules/',  views.update_rules, name="hello_world"),

]
