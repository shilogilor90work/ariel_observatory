
from django.urls import path
from . import views


urlpatterns = [
    path('',  views.status_view, name="dashboard"),
    path('rules/',  views.rules_view, name="rules"),
    path('api/',  views.api_view_test, name="api"),
    path('rules/hello_world/',  views.hello_world, name="hello_world"),
    path('rules/update_rules/',  views.update_rules, name="hello_world"),

]
