from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    # overview
    path('overview/', include('overview.urls')),
    # top keywords
    path('topword/', include('app_top_keyword.urls')),
    # app top persons
    path('topperson/', include('app_top_person.urls')),
    # user keyword analysis
    path('userkeyword/', include('app_user_keyword.urls')),
    # full text search and associated keyword display
    path('userkeyword_assoc/', include('app_user_keyword_association.urls')),
    # full text search and setiment keyword display
    path('userkeyword_senti/', include('app_user_keyword_sentiment.urls')),
    # top rank of people
    path('toprank/', include('app_top_rank.urls')),
    # sentiment bert
    path('sentiment/', include('app_sentiment_bert.urls')),
    # top person in yesterday
    path('toppersonYesterday/', include('app_top_person_yesterday.urls')),
]
