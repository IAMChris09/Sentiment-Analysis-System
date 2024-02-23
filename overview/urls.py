from django.urls import path
from overview import views

app_name="overview"

urlpatterns = [
    # top (popular) persons
    path('', views.home, name='home'),
    # ajax path
]

