from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd

# render渲染網頁


def home(request):
    return render(request,
                  'app_top_keyword/home.html')


# read df
df_topkey = pd.read_csv('app_top_keyword/dataset/top_key.csv', sep=',')

# prepare data
data = {}
for idx, row in df_topkey.iterrows():
    data[row['category']] = eval(row['top_keys'])

# We don't use it anymore, so delete it to save memory.
del df_topkey

# POST: csrf_exempt should be used
# 指定這一支程式忽略csrf驗證

@csrf_exempt
def api_get_cate_topword(request):
    cate = request.POST.get('news_category')
    # cate = request.GET['news_category'] # this command also works.
    topk = request.POST.get('topk')
    topk = int(topk)
    print(cate, topk)

    chart_data, wf_pairs = get_category_topword(cate, topk)
    response = {'chart_data': chart_data,
                'wf_pairs': wf_pairs,
                }
    print(response)
    return JsonResponse(response)


def get_category_topword(cate, topk=10):
    wf_pairs = data[cate][0:topk]
    words = [w for w, f in wf_pairs]
    freqs = [f for w, f in wf_pairs]
    chart_data = {
        "category": cate,
        "labels": words,
        "values": freqs}
    return chart_data, wf_pairs


print("app_top_keywords--類別熱門關鍵字載入成功!")

# # When Post is used, the csrf of this function should be ignored

# ne_name =['EVENT','FAC','GPE','LANGUAGE','LAW','LOC','NORP','ORG','PERSON','PRODUCT','WORK_OF_ART']
# idx2nename = { str(i) : item for i, item in enumerate(ne_name)}

# news_categories=['政治','科技','運動','證卷','產經','娛樂','生活','國際','社會','文化','兩岸','全部']
# idx2cate = { str(i) : item for i, item in enumerate(news_categories)}

# @csrf_exempt
# def api_get_ner_topword(request):
#     # POST方式取得新聞類別
#     cate = request.POST.get('news_category')
#     cate = idx2cate[cate]

#     # 取得多少筆關鍵詞
#     topk = int(request.POST.get('topk'))

#     ner_value = request.POST.get('ner_value')
#     ner_value = idx2nename[ner_value]

#     print(ner_value, cate, topk)

#     responseData = get_category_topkey(ner_value, cate, topk)
#     response = {'data': responseData}
#     print(response)
#     return JsonResponse(response)

# def get_category_topkey(ner_value, cate, topk):

#     wf_pairs = data[ner_value][cate][0:topk]

#     if wf_pairs == []:
#         return []

#     words = [w for w, f in wf_pairs]
#     freqs = [f for w, f in wf_pairs]

#     # Prepare cloud chart data
#     # the minimum and maximum frequency of top words
#     min_ = wf_pairs[-1][1]  # the last line is smaller
#     max_ = wf_pairs[0][1]   # the first frequency value is larger

#     textSizeMin = 10
#     textSizeMax = 90

#     if (min_ != max_):
#         max_min_range = max_ - min_

#     else:
#         max_min_range = len(wf_pairs)
#         min_ = min_ - 1

#     # cloud chart data
#     # using proportional scaling
#     clouddata = [{'text':w, 'size':int(textSizeMin+(f - min_)/max_min_range*(textSizeMax-textSizeMin))} for w, f in wf_pairs]

#     responseData = {
#         "wf_pairs": wf_pairs,
#         "data_barchart":{
#                         "category": cate,
#                         "labels": words,
#                         "values": freqs
#                         },
#         "data_cloud": clouddata}
#     return responseData

df_topkey = pd.read_csv('app_top_keyword/dataset/top_key.csv', sep=',')