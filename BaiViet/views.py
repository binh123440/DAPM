from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.utils import timezone
from PIL import Image
from django.db.models import Q
import pytesseract
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import render, get_object_or_404
# Create your views here.
pytesseract.pytesseract.tesseract_cmd = r'D:\TestWebPython\tesseract\tesseract.exe'

def get_BaiViet(request):
    hinhanhs = HinhAnh.objects.all()
    
    search_query = request.GET.get('search', '')

    if search_query:
        Baiviets2 = BaiViet.objects.all()
        Baiviets3 = BaiViet.objects.all()
        baiviets2 = Baiviets2.filter(Q(TieuDe__icontains=search_query))
        baiviets = BaiViet.objects.none()
    else:
        baiviets = BaiViet.objects.all()[:3]
        baiviets2 = BaiViet.objects.all()[:5]
        Baiviets3 = BaiViet.objects.all()

    context = {
        'baiviets': baiviets,
        'baiviets2': baiviets2,
        'baiviets3': Baiviets3,
        'hinhanhs': hinhanhs
    }
    return render(request, 'app/BaiViet.html', context)

def get_DangKyHoSo(request):
    return render(request, 'app/DangKyHoSo.html')

# def view_bai_viet(request):
#     search_query = request.GET.get('search', '')
#     baiviets = BaiViet.objects.all()
#     hinhanhs = HinhAnh.objects.all()
#     if search_query:
#         baiviets = baiviets.filter(
#             Q(TieuDe__icontains=search_query)
#         )

#     context = {
#         'baiviets2': baiviets,'hinhanhs': hinhanhs
#     }
#     return render(request, 'app/BaiViet.html', context)

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
def detail(request, mbv):
    baiviet = get_object_or_404(BaiViet, MBV=mbv)
    quydinhapdung = QuyDinhApDung.objects.select_related('MDT', 'MTC').filter(MBV=baiviet)
    baivietkhac = BaiViet.objects.all()
    return render(request, 'app/detail.html', {'baiviet': baiviet,'quydinhapdung': quydinhapdung, 'baivietkhac' : baivietkhac})
# def luu_ho_so(request):
#     # Lấy thông tin từ form
#     ten = request.POST.get('ten')
#     msv = request.POST.get('msv')
#     email = request.POST.get('email')
#     sdt = request.POST.get('sdt')
    
#     # Tìm sinh viên từ mã sinh viên
#     sinh_vien = SinhVien.objects.get(MSV=msv)
    
#     # Tạo hồ sơ đăng ký mới
#     ho_so = HoSoDangKy(
#         MSV=sinh_vien,
#         MotaHoancanhKhokhan='Mô tả hoàn cảnh khó khăn',
#         TrangthaiXacnhan=0,
#         Ngaydangky=timezone.now().date(),
#         Hocki='223',
#     )
#     ho_so.save()
    
#     # Xử lý ảnh minh chứng
#     files = request.FILES.getlist('anh_minh_chung')
#     for file in files:
#         # Gửi ảnh lên API để nhận dạng văn bản
#         url = "https://text-in-images-recognition.p.rapidapi.com/prod"
#         files_payload = {'file': (file.name, file, file.content_type)}
#         headers = {
#             "X-RapidAPI-Key": "bd682c590bmshf92cbe60c015db8p1fd9d6jsn20635d0ef8ad",
#             "X-RapidAPI-Host": "text-in-images-recognition.p.rapidapi.com"
#         }
#         response = requests.post(url, json=files_payload, headers=headers)
        
#         # Kiểm tra nếu có văn bản trong ảnh
#         if response.json().get('text'):
#             # Lưu ảnh vào model HinhAnh
#             hinh_anh = HinhAnh(TenHA=file.name, HA=file)
#             hinh_anh.save()
            
#             # Liên kết ảnh với hồ sơ đăng ký
#             ho_so.hinhanh_set.add(hinh_anh)
    
#     return ho_so


# # # Sử dụng trong view
# # def dang_ky_ho_so(request):
# #     if request.method == 'POST':
# #         ho_so = luu_ho_so(request)
# #         # Xử lý sau khi lưu thành công


# @require_POST
# @csrf_exempt
# def dang_ky_ho_so(request):
#     # Kiểm tra nếu yêu cầu là từ AJAX
#     if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#         # Xử lý đăng ký hồ sơ
#         ho_so = luu_ho_so(request)
#         # Trả về phản hồi JSON
#         return JsonResponse({'success': True})
#     else:
#         # Trả về phản hồi không hợp lệ cho yêu cầu không phải AJAX
#         return JsonResponse({'success': False, 'error': 'Yêu cầu không hợp lệ'}, status=400)
def get_DangKyHoSo(request):
    loai_doi_tuong_chinh_sach = LoaiDoiTuongChinhSach.objects.all()
    doi_tuong_chinh_sach = DoiTuongChinhSach.objects.all()
    context = {
        'loai_doi_tuong_chinh_sach': loai_doi_tuong_chinh_sach,
        'doi_tuong_chinh_sach': doi_tuong_chinh_sach,
    }
    return render(request, 'app/DangKyHoSo.html', context)

@csrf_exempt
def luu_ho_so_dang_ky(request):
    if request.method == 'POST':
        # Lấy thông tin từ form
        ho_ten = request.POST.get('ho_ten')
        ma_sinh_vien = request.POST.get('ma_sinh_vien')
        email = request.POST.get('email')
        so_dien_thoai = request.POST.get('so_dien_thoai')
        dia_chi = request.POST.get('dia_chi')
        hinh_anh = request.FILES.getlist('hinh_anh')
        ma_doi_tuong = request.POST.get('doi_tuong_chinh_sach')
       
       

        print(ma_doi_tuong)
        # Tìm sinh viên từ mã sinh viên
        
        try:
           sinh_vien = SinhVien.objects.get(MSV=ma_sinh_vien)
        except SinhVien.DoesNotExist:
    # Xử lý trường hợp không tìm thấy đối tượng
            return JsonResponse({'success': False, 'error': 'Mã sinh viên không tồn tại'})
        pass
        # Trích xuất văn bản từ hình ảnh
        mota_hoan_canh_kho_khan = ''
        for anh in hinh_anh:
            img = Image.open(anh)
            text = pytesseract.image_to_string(img)
            print(text)
            if text == "":
                return JsonResponse({'success': False, 'error': 'Hình ảnh không nhận được chữ'}); break
            mota_hoan_canh_kho_khan += text

        doi_tuong = DoiTuongChinhSach.objects.get(MDT=ma_doi_tuong)
        mdt = doi_tuong.MDT

        # Tạo hồ sơ đăng ký mới
        ho_so_dang_ky = HoSoDangKy.objects.create(
            MSV=sinh_vien,
            MotaHoancanhKhokhan=mota_hoan_canh_kho_khan,
            TrangthaiXacnhan=0,
            Ngaydangky=timezone.now().date(),
            Hocki='223',
            MDT = doi_tuong
        )

        # Lưu hình ảnh vào model HinhAnh và liên kết với hồ sơ đăng ký
        hinh_anh_objects = []
        for anh in hinh_anh:
            hinh_anh_moi = HinhAnh.objects.create(
                TenHA=anh.name,
                HA=anh
            )
            hinh_anh_objects.append(hinh_anh_moi)

            # Tạo và lưu chi tiết hồ sơ
            chi_tiet_ho_so = ChiTietHoSo.objects.create(
                MHSDK=ho_so_dang_ky,
                MTC=None,  # Giả sử bạn chưa có TieuChi, hãy thay đổi phù hợp
                MHA=hinh_anh_moi
            )

        # Trả về phản hồi thành công
        return JsonResponse({'success': True})
    else:
        # Trả về phản hồi lỗi cho các phương thức khác
        return JsonResponse({'success': False, 'error': 'Phương thức không hợp lệ'})
    


#     @csrf_exempt
# def luu_ho_so_dang_ky(request):
#     if request.method == 'POST':
#         # Lấy thông tin từ form
#         ho_ten = request.POST.get('ho_ten')
#         ma_sinh_vien = request.POST.get('ma_sinh_vien')
#         email = request.POST.get('email')
#         so_dien_thoai = request.POST.get('so_dien_thoai')
#         dia_chi = request.POST.get('dia_chi')
#         hinh_anh = request.FILES.getlist('hinh_anh')

#         # Tìm sinh viên từ mã sinh viên
#         sinh_vien = SinhVien.objects.get(MSV=ma_sinh_vien)

#         # Trích xuất văn bản từ hình ảnh
#         mota_hoan_canh_kho_khan = ''
#         for anh in hinh_anh:
#             img = Image.open(anh)
#             text = pytesseract.image_to_string(img)
#             mota_hoan_canh_kho_khan += text

#         # Tạo hồ sơ đăng ký mới
#         ho_so_dang_ky = HoSoDangKy.objects.create(
#             MSV=sinh_vien,
#             MotaHoancanhKhokhan=mota_hoan_canh_kho_khan,
#             TrangthaiXacnhan=0,
#             Ngaydangky=timezone.now().date(),
#             Hocki='223'
#         )

#         # Lưu hình ảnh vào model HinhAnh và liên kết với hồ sơ đăng ký
#         hinh_anh_objects = []
#         for anh in hinh_anh:
#             hinh_anh_moi = HinhAnh.objects.create(
#                 TenHA=anh.name,
#                 HA=anh
#             )
#             hinh_anh_objects.append(hinh_anh_moi)

#             # Tạo và lưu chi tiết hồ sơ
#             chi_tiet_ho_so = ChiTietHoSo.objects.create(
#                 MHSDK=ho_so_dang_ky,
#                 MTC=None,  # Giả sử bạn chưa có TieuChi, hãy thay đổi phù hợp
#                 MHA=hinh_anh_moi
#             )

#         # Trả về phản hồi thành công
#         return JsonResponse({'success': True})
#     else:
#         # Trả về phản hồi lỗi cho các phương thức khác
#         return JsonResponse({'success': False, 'error': 'Phương thức không hợp lệ'})