from django.urls import include, path
from NEWS.views import *


urlpatterns = [
    path('', news_home, name = 'news_home'),
    path('create', create, name = 'create'),
    path('<int:pk>', NewsDetailView.as_view(), name='news-detail')
] 