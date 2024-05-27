from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import *
from datetime import date
from django.utils import timezone
import requests
from django.shortcuts import render, redirect
# Create your views here.

def get_BaiViet(request):
    hinhanhs = HinhAnh.objects.all()
    baiviets = BaiViet.objects.all()[:3]
    context = {'baiviets': baiviets, 'hinhanhs': hinhanhs}
    return render(request, 'app/BaiViet.html', context)
def get_DangKyHoSo(request):
    return render(request, 'app/DangKyHoSo.html')

def load_more_posts(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        offset = int(request.GET.get('offset', 0))
        limit = 3
        baiviets = BaiViet.objects.all()[offset:offset+limit]
        data = []
        for baiviet in baiviets:
            data.append({
                'AnhBia': baiviet.AnhBia.url,
                'TieuDe': baiviet.TieuDe,
                'Ngaydang': baiviet.Ngaydang.strftime('%d/%m/%Y'),
            })
        return JsonResponse(data, safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def luu_ho_so(request):
    # Lấy thông tin từ form
    ten = request.POST.get('ten')
    msv = request.POST.get('msv')
    email = request.POST.get('email')
    sdt = request.POST.get('sdt')
    
    # Tìm sinh viên từ mã sinh viên
    sinh_vien = SinhVien.objects.get(MSV=msv)
    
    # Tạo hồ sơ đăng ký mới
    ho_so = HoSoDangKy(
        MSV=sinh_vien,
        MotaHoancanhKhokhan='Mô tả hoàn cảnh khó khăn',
        TrangthaiXacnhan=0,
        Ngaydangky=timezone.now().date(),
        Hocki='223',
    )
    ho_so.save()
    
    # Xử lý ảnh minh chứng
    files = request.FILES.getlist('anh_minh_chung')
    for file in files:
        # Gửi ảnh lên API để nhận dạng văn bản
        url = "https://text-in-images-recognition.p.rapidapi.com/prod"
        files_payload = {'file': (file.name, file, file.content_type)}
        headers = {
            "X-RapidAPI-Key": "bd682c590bmshf92cbe60c015db8p1fd9d6jsn20635d0ef8ad",
            "X-RapidAPI-Host": "text-in-images-recognition.p.rapidapi.com"
        }
        response = requests.post(url, json=files_payload, headers=headers)
        
        # Kiểm tra nếu có văn bản trong ảnh
        if response.json().get('text'):
            # Lưu ảnh vào model HinhAnh
            hinh_anh = HinhAnh(TenHA=file.name, HA=file)
            hinh_anh.save()
            
            # Liên kết ảnh với hồ sơ đăng ký
            ho_so.hinhanh_set.add(hinh_anh)
    
    return ho_so


# # Sử dụng trong view
# def dang_ky_ho_so(request):
#     if request.method == 'POST':
#         ho_so = luu_ho_so(request)
#         # Xử lý sau khi lưu thành công


@require_POST
@csrf_exempt
def dang_ky_ho_so(request):
    # Kiểm tra nếu yêu cầu là từ AJAX
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Xử lý đăng ký hồ sơ
        ho_so = luu_ho_so(request)
        # Trả về phản hồi JSON
        return JsonResponse({'success': True})
    else:
        # Trả về phản hồi không hợp lệ cho yêu cầu không phải AJAX
        return JsonResponse({'success': False, 'error': 'Yêu cầu không hợp lệ'}, status=400)
