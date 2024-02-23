from django.http import JsonResponse
import pandas as pd
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def load_data_pk():
    # Read data from csv file
    df_data_pk = pd.read_csv('app_top_rank/dataset/pk_taipei_mayor_election.csv')
    
    global data
    data={}
    for k,v in zip(df_data_pk.name, df_data_pk.value):
        data[k]=eval(v)
    
    # 沒用到的變數刪除之
    del df_data_pk

# load pk data
load_data_pk()

def home(request):
    return render(request,'app_top_rank/home.html')

# csrf_exempt is used for POST
# 單獨指定這一支程式忽略csrf驗證
@csrf_exempt
def app_top_rank(request):
    return JsonResponse(data)

print('Load app top rank people leaderboard...')
