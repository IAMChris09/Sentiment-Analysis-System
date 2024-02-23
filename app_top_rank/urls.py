from django.urls import path
from app_top_rank import views

# app_name='namespace_taipei_mayor'
app_name='app_top_rank'

urlpatterns = [
    path('', views.home, name='home'),
    path('app_top_rank/', views.app_top_rank),
]
