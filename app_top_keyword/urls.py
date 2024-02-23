from django.urls import path
from app_top_keyword import views

# declare a  namespace for this APP
# the name of namespace is  'app_top_keyword'
# We will use the namespace in the future integrated website.
app_name = 'app_top_keyword'

urlpatterns = [
    # For home
    path('', views.home, name='home'),
    # For Ajax
    path('api_get_cate_topword/', views.api_get_cate_topword),
    # path('api_get_ner_topword/', views.api_get_ner_topword),
]
