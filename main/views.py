# main/views.py
from django.shortcuts import render, get_object_or_404
from .models import DailyFlyer, Page
from django.db.models import Q

def home(request):
    flyers = DailyFlyer.objects.order_by('-id')  # جلب جميع المنشورات مرتبة حسب الأحدث
    return render(request, 'main/home.html', {'flyers': flyers})

def page_view(request, page_area):
    pages = Page.objects.filter(area=page_area)  # جلب جميع الصفحات للمنطقة المحددة
    return render(request, 'main/page.html', {'pages': pages, 'area': page_area})

def news_detail(request, flyer_id):
    flyer = get_object_or_404(DailyFlyer, id=flyer_id)
    return render(request, 'main/news_detail.html', {'flyer': flyer})
