# main/urls.py
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('الباب/', views.page_view, {'page_area': 'الباب'}, name='page_bab'),
    path('جنديرس/', views.page_view, {'page_area': 'جنديرس'}, name='page_jandirs'),
    path('news/<int:flyer_id>/', views.news_detail, name='news_detail'),
]
