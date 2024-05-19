from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from .models import BaiViet
from datetime import datetime

def index(request):
    query = request.GET.get('q')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    baiviet = BaiViet.objects.select_related('MNV')
    if query:
        keywords = query.split()
        query_filter = Q()
        for keyword in keywords:
            query_filter |= Q(Noidung__icontains=keyword) | Q(MNV__Hoten__icontains=keyword)
        baiviet = baiviet.filter(query_filter)  
    if start_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        baiviet = baiviet.filter(Ngaydang__date=start_date)
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        baiviet = baiviet.filter(NgayhetHieuluc__date=end_date)
    if not query and not start_date and not end_date:
        baiviet = baiviet[:2]

    return render(request, 'app/index.html', {'baiviet': baiviet, 'query': query, 'start_date': start_date, 'end_date': end_date})
# def bai_viet_detail(request, mbv):
#     bai_viet = get_object_or_404(BaiViet, MBV=mbv)
#     return render(request, 'bai_viet_detail.html', {'bai_viet': bai_viet})