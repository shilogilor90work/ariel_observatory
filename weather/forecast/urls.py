
from django.urls import path
from . import views


urlpatterns = [
    path('',  views.status_view, name="dashboard"),
    path('rules',  views.rules_view, name="rules"),
]
