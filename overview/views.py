from django.shortcuts import render
from django.http import  JsonResponse
import pandas as pd

# render��V����
def home(request):
    return render(request, 'overview/home.html')
