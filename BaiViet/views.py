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
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import SinhVienForm, DaiDienPhongBanForm
import calendar
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

    if request.session.get('username') is not None:
            user_id = request.session.get('username')
            user = SinhVien.objects.get(MSV=user_id)
    else:
            user_id = None
            user = None
    context = {
        'baiviets': baiviets,
        'baiviets2': baiviets2,
        'baiviets3': Baiviets3,
        'sinh_vien': user,
        'hinhanhs': hinhanhs
        
    }
    return render(request, 'app/BaiViet.html', context)

def get_DangKyHoSo(request):
    loai_doi_tuong_chinh_sach = LoaiDoiTuongChinhSach.objects.all()
    doi_tuong_chinh_sach = DoiTuongChinhSach.objects.all()

    if request.session.get('username') is not None:
            # user_id = request.session.get('username')
            # user = SinhVien.objects.get(MSV=user_id)
            return redirect('base')
    else:
            user_id = None
            user = None


    context = {
        'loai_doi_tuong_chinh_sach': loai_doi_tuong_chinh_sach,
        'doi_tuong_chinh_sach': doi_tuong_chinh_sach,
        'sinh_vien': user,
    }
    return render(request, 'app/DangKyHoSo.html', context)
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
                'MBV': baiviet.MBV,
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
        baiviet = baiviet.filter(Ngaydang=start_date)
    if end_date:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        baiviet = baiviet.filter(NgayhetHieuluc=end_date)
    if not query and not start_date and not end_date:
        baiviet = baiviet[:2]

    if request.session.get('username') is not None:
            # user_id = request.session.get('username')
            # user = SinhVien.objects.get(MSV=user_id)
            return redirect('base')
    else:
            user_id = None
            user = None

    context = {
        'sinh_vien': user,
        'baiviet': baiviet, 
        'query': query, 
        'start_date': start_date, 
        'end_date': end_date
    }
    return render(request, 'app/index2.html', context)

def detail(request, mbv):
    baiviet = get_object_or_404(BaiViet, MBV=mbv)
    quydinhapdung = QuyDinhApDung.objects.select_related('MDT', 'MTC').filter(MBV=baiviet)
    baivietkhac = BaiViet.objects.all()

    
    if request.session.get('username') is not None:
            user_id = request.session.get('username')
            user = SinhVien.objects.get(MSV=user_id)
    else:
            user_id = None
            user = None

    context = {
        'sinh_vien': user,
        'baiviet': baiviet,
        'quydinhapdung': quydinhapdung, 
        'baivietkhac' : baivietkhac
    }
    return render(request, 'app/detail.html', context)
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
        ma_nhan_vien = DaiDienPhongBan.objects.get(MNV='01')
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
        if hinh_anh:
            for anh in hinh_anh:
                img = Image.open(anh)
                text = pytesseract.image_to_string(img, lang='vie')
                print(text)
                if text == "" or text == None:
                    return JsonResponse({'success': False, 'error': 'Hình ảnh không nhận được chữ'}); break
                mota_hoan_canh_kho_khan += text
        else:
            return JsonResponse({'success': False, 'error': 'Chưa thêm hình ảnh'})
        doi_tuong = DoiTuongChinhSach.objects.get(MDT=ma_doi_tuong)
        mdt = doi_tuong.MDT

        # Tạo hồ sơ đăng ký mới
        ho_so_dang_ky = HoSoDangKy.objects.create(
            MSV=sinh_vien,
            MotaHoancanhKhokhan=mota_hoan_canh_kho_khan,
            TrangthaiXacnhan=0,
            Ngaydangky=datetime.now(),
            Hocki='223',
            MNV=ma_nhan_vien,
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

def chinhsuathongtin(request, MSV):
    sinhvien = get_object_or_404(SinhVien, MSV=MSV)
    if request.method == 'POST':
        
        msv = request.POST.get('MSV')
        hoten = request.POST.get('Hoten')
        ngaysinh_str = request.POST.get('Ngaysinh')
        gioitinh = request.POST.get('Gioitinh')
        dantoc = request.POST.get('Dantoc')
        sdt = request.POST.get('SDT')
        email = request.POST.get('Email')
        lop = request.POST.get('Lopsinhhoat')
        khoa = request.POST.get('Khoa')
        nienkhoa = request.POST.get('Nienkhoa')
        quequan = request.POST.get('Quequan')
        matkhau = request.POST.get('Matkhau')
        image = request.FILES.get('Image')
        try:
            ngaysinh = datetime.strptime(ngaysinh_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Ngày sinh không hợp lệ. Vui lòng nhập theo định dạng YYYY-MM-DD.")
            return JsonResponse({'success': False})

        # Cập nhật thông tin sinh viên
        sinhvien.MSV = msv
        sinhvien.Hoten = hoten
        sinhvien.Ngaysinh = ngaysinh
        sinhvien.Gioitinh = int(gioitinh)
        sinhvien.Dantoc = dantoc
        sinhvien.SDT = sdt
        sinhvien.Email = email
        sinhvien.Lopsinhhoat = lop
        sinhvien.Khoa = khoa
        sinhvien.Nienkhoa = nienkhoa
        sinhvien.Quequan = quequan
        if matkhau:
            sinhvien.Pass = matkhau
        if image:
            sinhvien.Image = image
        sinhvien.save()
        return JsonResponse({'success': True, 'message': "Cập nhật thông tin thành công!"})
    else:
        context = {'sinhvien': sinhvien}
        return render(request, 'app/chinhsuathongtin.html', context)
    
def thongtinphongCTSV(request, MNV):
    phongctvs = get_object_or_404(DaiDienPhongBan, MNV=MNV)
    if request.method == 'POST':
        
        mnv = request.POST['MNV']
        hoten = request.POST['Hoten']
        ngaysinh_str = request.POST['Ngaysinh']
        gioitinh = request.POST['Gioitinh']
        sdt = request.POST['SDT']
        email = request.POST['Email']
        matkhau = request.POST['Matkhau']
        image = request.FILES.get('Image')
        try:
            ngaysinh = datetime.strptime(ngaysinh_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Ngày sinh không hợp lệ. Vui lòng nhập theo định dạng YYYY-MM-DD.")
            return JsonResponse({'success': False})

        # Cập nhật thông tin sinh viên
        phongctvs.MNV = mnv
        phongctvs.Hoten = hoten
        phongctvs.Ngaysinh = ngaysinh
        phongctvs.Gioitinh = int(gioitinh)
        phongctvs.SDT = sdt
        phongctvs.Email = email
        phongctvs.Pass = matkhau
        if image:
            phongctvs.Image = image
        phongctvs.save()

        return JsonResponse({'success': True, 'message': "Cập nhật thông tin thành công!"})

    context = {'phongctvs': phongctvs}
    return render(request, 'app/thongtinphongCTSV.html', context)

def thongtinphongBGH(request, MNV):
    bgh = get_object_or_404(DaiDienPhongBan, MNV=MNV)
    if request.method == 'POST':
        
        mnv = request.POST['MNV']
        hoten = request.POST['Hoten']
        ngaysinh_str = request.POST['Ngaysinh']
        gioitinh = request.POST['Gioitinh']
        sdt = request.POST['SDT']
        email = request.POST['Email']
        chucvu = request.POST['Roles']
        matkhau = request.POST['Matkhau']
        image = request.FILES.get('Image')
        try:
            ngaysinh = datetime.strptime(ngaysinh_str, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Ngày sinh không hợp lệ. Vui lòng nhập theo định dạng YYYY-MM-DD.")
            return JsonResponse({'success': False})

        # Cập nhật thông tin sinh viên
        bgh.MNV = mnv
        bgh.Hoten = hoten
        bgh.Ngaysinh = ngaysinh
        bgh.Gioitinh = int(gioitinh)
        bgh.SDT = sdt
        bgh.Email = email
        bgh.Roles = chucvu
        bgh.Pass = matkhau
        if image:
            bgh.Image = image
        bgh.save()

        return JsonResponse({'success': True, 'message': "Cập nhật thông tin thành công!"})

    context = {'bgh': bgh}
    return render(request, 'app/thongtinphongBGH.html', context)



def signin(request):
    if request.method == "GET":
        username_login = request.GET.get('username')
        password_login = request.GET.get('Pass')
        
        print(f"Username: {username_login}, Password: {password_login}")  # In ra giá trị để kiểm tra
        
        if username_login is None or password_login is None:
            return render(request, "app/signin.html")
        elif len(username_login) == 0:
            return HttpResponse("Username is required", status=400)
        if len(username_login) > 10:
            try:
                sinh_vien = SinhVien.objects.get(MSV=username_login, Pass=password_login)
                request.session['username'] = sinh_vien.MSV
                
                return redirect('base')
            except SinhVien.DoesNotExist:
                print("Không có sinh viên có mã sv tồn tại")
            except SinhVien.MultipleObjectsReturned:
                print("Có nhiều hơn 1 sinh viên có msv sau")
        else:
            try:
                nhan_vien = DaiDienPhongBan.objects.get(MNV=username_login, Pass=password_login)   
                request.session['username'] = nhan_vien.MNV
                return redirect('base')
            except DaiDienPhongBan.DoesNotExist:
                print("Không có nhân viên có mã nv tồn tại")
            except DaiDienPhongBan.MultipleObjectsReturned:
                print("Có nhiều hơn 1 nhân viên có mnv sau")
    return render(request, "app/signin.html")
     
def logout(request):
    request.session.flush()
    if 'username' in request.session:
        del request.session['username']
    return redirect('index')     
            
def signup(request):
    if request.method == 'POST':
        form = SinhVienForm(request.POST)
        if form.is_valid():
            msv = form.cleaned_data['MSV']
            hoten = form.cleaned_data['Hoten']
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Pass']
            


            sinhvien, created = SinhVien.objects.get_or_create(MSV=msv, defaults={
                'Hoten': hoten,
                'Email': email,
                'Pass': password,
            })

            if not created:
                # Nếu không tạo được đối tượng mới (MSV đã tồn tại)
                messages.error(request, 'Mã sinh viên này đã tồn tại trong hệ thống.')
                return render(request, 'app/signup.html', {'form': form})
            else:
                sinhvien = SinhVien(MSV=msv, Hoten=hoten, Email=email, Pass=password)
                sinhvien.save()
            
            request.session['username'] = form.cleaned_data['MSV']
            print(request.session['username'])
            
            # Tạo một instance mới của SinhVien và lưu vào cơ sở dữ liệu
            # sinhvien = SinhVien(MSV=msv, Hoten=hoten, Email=email, Pass=password)
            # sinhvien.save()
            # Chuyển hướng người dùng đến trang khác sau khi đăng ký thành công
            return redirect('base')  # Thay 'base' bằng tên của URLpattern bạn muốn chuyển hướng đến
    else:
        form = SinhVienForm()
        
    context = {
        'form' : form
    }
    
    return render(request, "app/signup.html", context)

def update_hs(request, mahs):
    if request.method == "POST":
        hs = HoSoDangKy.objects.get(MHSDK = mahs)
        hs.MNV = DaiDienPhongBan.objects.get(pk=request.session.get('username'))
        hs.TrangthaiXetduyet = 0
        hs.Ngayxetduyet = datetime.now()
        hs.save()
        return redirect('base')
    else:
        print('Hồ sơ chưa cập nhật thành công')

def view_detail(request, mahs):
    hs = HoSoDangKy.objects.get(MHSDK = mahs)
    sv = hs.MSV
    nv_xet_duyet = hs.MNV
    nv = DaiDienPhongBan.objects.get(MNV = request.session.get('username'))
    dt = hs.MDT
        
    hs_object = {
        'date': hs.Ngaydangky.date().strftime('%Y-%m-%d'),
        'time': hs.Ngaydangky.time().strftime('%H:%M:%S')
    }
    
    print(hs.Ngaydangky.date())
    print(hs.Ngaydangky.time())
              
    context = {
        'hs' : hs,
        'sv' : sv,
        'nv' : nv,
        'dt' : dt,
        'hs_object' : hs_object,
        'nv_xet_duyet' : nv_xet_duyet
    }
    return render(request, 'app/view_detail.html', context)

# def login(request):
#     if request.method == 'POST':
#         form = SinhVienForm(request.POST)
#         if form.is_valid():
#             msv = form.cleaned_data['MSV']
#             hoten = form.cleaned_data['Hoten']
#             email = form.cleaned_data['Email']
#             password = form.cleaned_data['Pass']
            
#             request.session['username'] = form.cleaned_data['MSV']
#             print(request.session['username'])
            
#             # Tạo một instance mới của SinhVien và lưu vào cơ sở dữ liệu
#             sinhvien = SinhVien(MSV=msv, Hoten=hoten, Email=email, Pass=password)
#             sinhvien.save()
#             # Chuyển hướng người dùng đến trang khác sau khi đăng ký thành công
#             return redirect('base')  # Thay 'base' bằng tên của URLpattern bạn muốn chuyển hướng đến
#     elif request.method == "GET":
#         username_login = request.GET.get('username')
#         password_login = request.GET.get('password')
        
#         print(f"Username: {username_login}, Password: {password_login}")  # In ra giá trị để kiểm tra

#         sinh_vien_s = SinhVien.objects.all()
#         nhan_vien_s = DaiDienPhongBan.objects.all()
        
#         if username_login is None or password_login is None:
#             return render(request, "app/login.html")
#         elif len(username_login) == 0:
#             return HttpResponse("Username is required", status=400)
#         elif len(username_login) <= 10:
#             for nv in nhan_vien_s:
#                 if username_login == nv.MNV and password_login == nv.Pass:
#                     if 'username' in request.session:
#                         del request.session['username']
#                     else:
#                         request.session['username'] = nv.MNV
#                     print(f"Nhan vien login: {request.session['username']}")
#                     return redirect('base')  # Thay 'base' bằng tên của URLpattern bạn muốn chuyển hướng đến
#         else:
#             for sv in sinh_vien_s:
#                 if username_login == sv.MSV and password_login == sv.Pass:
#                     request.session['username'] = sv.MSV
#                     print(f"Sinh vien login: {request.session['username']}")
#                     return redirect('index')  # Thay 'base' bằng tên của URLpattern bạn muốn chuyển hướng đến
                
#     return render(request, "app/login.html")

def base(request):
    hs_s = HoSoDangKy.objects.all()
    total_hs = hs_s.count()
    
    username = request.session.get('username')
    print(username)
    
    if len(username) > 10:
        try:
            user = SinhVien.objects.get(MSV=username)
            print(f"Found sinh_vien: {user}")
            request.session['username'] = user.MSV
            Baiviets2 = BaiViet.objects.all()[:2]
            context = {
                'baiviet': Baiviets2,
                'sinh_vien': user,
            }
            return render(request, 'app/Index2.html', context)
        except SinhVien.DoesNotExist:
            print("Không có sinh viên có msv tồn tại")
        except SinhVien.MultipleObjectsReturned:
            print("Có nhiều hơn 1 sv tồn tại với msv")
    else:
        try:
            user = DaiDienPhongBan.objects.get(MNV=username)
            print(f"Found nhan_vien: {user}")
            request.session['user_type'] = 'nhan_vien'
            request.session['user_id'] = user.MNV
        except DaiDienPhongBan.DoesNotExist:
            print("Không có nhân viên có mnv tồn tại")
        except DaiDienPhongBan.MultipleObjectsReturned:
            print("Có nhiều hơn 1 nv tồn tại với mnv")
    
    hs_objects = HoSoDangKy.objects.select_related('MSV', 'MNV')
    query = request.GET.get('query')
    if query:
        keywords = query.split()
        query_filter = Q()
        for keyword in keywords:
            query_filter |= Q(MSV__Hoten__icontains=keyword) | Q(MNV__Hoten__icontains=keyword)
        hs_objects = hs_objects.filter(query_filter)  

    
    # for hs in hs_s:
    #     mahs = hs.MHSDK
    #     sinh_vien = hs.MSV
    #     ten_sinh_vien = sinh_vien.Hoten
    #     trang_thai_xac_nhan = hs.TrangthaiXacnhan
    #     ngay_dang_ky = hs.Ngaydangky.date()
    #     thoi_gian_dang_ky = hs.Ngaydangky.time()
    #     nhan_vien = hs.MNV
    #     ten_nhan_vien = nhan_vien.Hoten
    #     if hs.Ngayxetduyet is not None:
    #         ngay_xet_duyet = hs.Ngayxetduyet.date()
    #         thoi_gian_xet_duyet = hs.Ngayxetduyet.time()
    #     else:
    #         ngay_xet_duyet = None
    #         thoi_gian_xet_duyet = None
    #     if hs.TrangthaiXetduyet is not None:
    #         trang_thai_xet_duyet = hs.TrangthaiXetduyet
    #     else:
    #         trang_thai_xet_duyet = None

    #     hs_objects.append({
    #         'MaHS' : mahs,
    #         'TenSV' : ten_sinh_vien,
    #         'TrangthaiXacnhan' : trang_thai_xac_nhan,
    #         'Ngaydangky' : ngay_dang_ky,
    #         'ThoigianDangky' : thoi_gian_dang_ky,
    #         'Tennhanvien' : ten_nhan_vien,
    #         'Ngayxetduyet' : ngay_xet_duyet,
    #         'ThoigianXetduyet' : thoi_gian_xet_duyet,
    #         'TrangthaiXetduyet' : trang_thai_xet_duyet,
    #     })
    
    
    total_hs_valid = 0
    total_hs_invalid = 0
    total_hs_success = 0
    total_hs_unsuccess = 0
    for hs in hs_s:
        if hs.TrangthaiXacnhan == 0:
            total_hs_valid += 1 
        elif hs.TrangthaiXacnhan == 1: 
            total_hs_invalid += 1
            
        if hs.TrangthaiXetduyet == 0:
            total_hs_success +=1
        elif hs.TrangthaiXetduyet == 1:
            total_hs_unsuccess += 1   
        
    percent_hs_valid = round((total_hs_valid/total_hs) * 100, 2)
    percent_hs_invalid = round((total_hs_invalid/total_hs) * 100, 2)
    percent_hs_success = round((total_hs_success/total_hs) * 100, 2)
    percent_hs_unsuccess = round((total_hs_unsuccess/total_hs) * 100, 2)
    
    current_month = datetime.now().month
    count_hs_valid = 0
    count_hs_invalid = 0
    count_hs_success = 0
    count_hs_unsuccess = 0
    count_hs_with_month1 = 0
    count_hs_with_month2 = 0
    count_hs_with_month3 = 0
    count_hs_with_month4 = 0
    hs_valid = []
    hs_invalid = []
    hs_success = []
    hs_unsuccess = []
    months_to_check = []
    months_to_check_str = []

    # Tạo danh sách các giá trị của tháng cần kiểm tra
    months_to_check = [(current_month - i) % 12 or 12 for i in range(4)]
    # Chuyển đổi số tháng thành tên tháng (dạng chuỗi)
    months_to_check_str = [calendar.month_abbr[month] for month in months_to_check]
    month1, month2, month3, month4 = months_to_check_str
    print(months_to_check_str)
    
    for hs in hs_s:
        if calendar.month_abbr[hs.Ngaydangky.month] == month1:
            count_hs_with_month1 += 1
        elif calendar.month_abbr[hs.Ngaydangky.month] == month2:
            count_hs_with_month2 += 1
        elif calendar.month_abbr[hs.Ngaydangky.month] == month3:
            count_hs_with_month3 += 1
        elif calendar.month_abbr[hs.Ngaydangky.month] == month4:
            count_hs_with_month4 += 1
                
    count_hs_1 = 0
    for hs in hs_s:
        if calendar.month_abbr[hs.Ngaydangky.month] == month1:
            count_hs_1 += 1
    # Lặp qua các tháng cần kiểm tra
    for month in months_to_check:
        # Đặt lại các biến đếm
        count_hs_valid = 0
        count_hs_invalid = 0
        count_hs_success = 0
        count_hs_unsuccess = 0
        
        for hs in hs_s:
            if hs.Ngaydangky.month == month:
                if hs.TrangthaiXacnhan == 0:
                    count_hs_valid += 1
                elif hs.TrangthaiXacnhan == 1:
                    count_hs_invalid += 1
                elif hs.TrangthaiXetduyet == 0:
                    count_hs_success += 1
                elif hs.TrangthaiXetduyet == 1:
                    count_hs_unsuccess += 1
        
        hs_valid.append(count_hs_valid)
        hs_invalid.append(count_hs_invalid)
        hs_success.append(count_hs_success)
        hs_unsuccess.append(count_hs_unsuccess)
        
    hs_invalid1, hs_invalid2, hs_invalid3, hs_invalid4 = hs_invalid
        
    hs_valid1, hs_valid2, hs_valid3, hs_valid4 = hs_valid
    if hs_valid2 != 0:
        percent_hs_valid_in_month_with_last_month = "tăng gấp " + str(round((hs_valid1 / hs_valid2) * 100, 1)) + " so với tháng trước"
    else:
        percent_hs_valid_in_month_with_last_month = "Không có hồ sơ nào hợp lệ tháng trước đó"  # Hoặc một giá trị nào đó bạn thấy hợp lý
    
    hs_success1, hs_success2, hs_success3, hs_success4 = hs_success
    if hs_success2 != 0:
        percent_hs_success_in_month_with_last_month = "tăng gấp " + round((hs_success1 / hs_success2) * 100, 1) + " so với tháng trước"
    else:
        percent_hs_success_in_month_with_last_month = "Không có hồ sơ nào thành công tháng trước đó"  # Hoặc một giá trị nào đó bạn thấy hợp lý
        
    hs_unsuccess1, hs_unsuccess2, hs_unsuccess3, hs_unsuccess4 = hs_success
    if hs_unsuccess2 != 0:
        percent_hs_unsuccess_in_month_with_last_month = "tăng gấp " + round((hs_unsuccess1 / hs_unsuccess2) * 100, 1) + " so với tháng trước"
    else:
        percent_hs_unsuccess_in_month_with_last_month = "Không có hồ sơ nào thành công tháng trước đó"  # Hoặc một giá trị nào đó bạn thấy hợp lý
    
    if count_hs_with_month2 != 0:
        percent_hs_in_month_with_last_month = round((count_hs_with_month1 / count_hs_with_month2) * 100, 1) 
    else:
        percent_hs_in_month_with_last_month = 0
    time_list_dk = []
    time_list_xd = []
    for hs in hs_s:
        if hs.Ngaydangky:
            # Tạo một từ điển với tháng và năm
            month_year = {
                'month': hs.Ngaydangky.month,
                'year': hs.Ngaydangky.year
            }
            
            # Kiểm tra xem month_year đã tồn tại trong time_list chưa
            if month_year not in time_list_dk:
                time_list_dk.append(month_year)
        if hs.Ngayxetduyet:
            # Tạo một từ điển với tháng và năm
            month_year = {
                'month': hs.Ngayxetduyet.month,
                'year': hs.Ngayxetduyet.year
            }
            
            # Kiểm tra xem month_year đã tồn tại trong time_list chưa
            if month_year not in time_list_xd:
                time_list_xd.append(month_year)
      
    context = {
        'hs_s' : hs_s,
        'total_hs' : total_hs,
        'total_hs_valid' : total_hs_valid,
        'total_hs_invalid' : total_hs_invalid,
        'total_hs_success' : total_hs_success,
        'total_hs_unsuccess' : total_hs_unsuccess,
        'percent_hs_valid' : percent_hs_valid,
        'percent_hs_invalid' : percent_hs_invalid,
        'percent_hs_success' : percent_hs_success,
        'percent_hs_unsuccess' : percent_hs_unsuccess,
        'hs_objects' : hs_objects,
        'username' : user,
        'hs_valid' : hs_valid,
        'hs_invalid' : hs_invalid,
        'hs_success' : hs_success,
        'hs_unsuccess' : hs_unsuccess,
        'month1' : month1,
        'month2' : month2,
        'month3' : month3,
        'month4' : month4,
        'count_hs_with_month1' : count_hs_with_month1,
        'count_hs_with_month2' : count_hs_with_month2,
        'count_hs_with_month3' : count_hs_with_month3,
        'count_hs_with_month4' : count_hs_with_month4,
        'percent_hs_in_month_with_last_month' : percent_hs_in_month_with_last_month,
        'percent_hs_valid_in_month_with_last_month' : percent_hs_valid_in_month_with_last_month,
        'percent_hs_success_in_month_with_last_month' : percent_hs_success_in_month_with_last_month,
        'percent_hs_unsuccess_in_month_with_last_month' : percent_hs_unsuccess_in_month_with_last_month,
        'hs_unsuccess1' : hs_unsuccess1,
        'hs_valid1' : hs_valid1,
        'hs_success1' : hs_success1,
        'hs1' : count_hs_1,
        'time_list_dk' : time_list_dk,
        'time_list_xd' : time_list_xd,
    }
    
    return render(request, 'app/base.html', context)
def charts(request):
    hs_s = HoSoDangKy.objects.all()
    total_hs = hs_s.count()
    
    hs_objects = []
    for hs in hs_s:
        sinh_vien = hs.MSV
        ten_sinh_vien = sinh_vien.Hoten
        trang_thai_xac_nhan = hs.TrangthaiXacnhan
        ngay_dang_ky = hs.Ngaydangky.date()
        thoi_gian_dang_ky = hs.Ngaydangky.time()
        nhan_vien = hs.MNV
        ten_nhan_vien = nhan_vien.Hoten
        if hs.Ngayxetduyet is not None:
            ngay_xet_duyet = hs.Ngayxetduyet.date()
            thoi_gian_xet_duyet = hs.Ngayxetduyet.time()
        else:
            ngay_xet_duyet = None
            thoi_gian_xet_duyet = None
        if hs.TrangthaiXetduyet is not None:
            trang_thai_xet_duyet = hs.TrangthaiXetduyet
        else:
            trang_thai_xet_duyet = None
        
        
        hs_objects.append({
            'TenSV' : ten_sinh_vien,
            'TrangthaiXacnhan' : trang_thai_xac_nhan,
            'Ngaydangky' : ngay_dang_ky,
            'ThoigianDangky' : thoi_gian_dang_ky,
            'Tennhanvien' : ten_nhan_vien,
            'Ngayxetduyet' : ngay_xet_duyet,
            'ThoigianXetduyet' : thoi_gian_xet_duyet,
            'TrangthaiXetduyet' : trang_thai_xet_duyet,
        })
    
    total_hs_valid = 0
    total_hs_invalid = 0
    total_hs_success = 0
    total_hs_unsuccess = 0
    for hs in hs_s:
        if hs.TrangthaiXacnhan == 0:
            total_hs_valid += 1 
        elif hs.TrangthaiXacnhan == 1: 
            total_hs_invalid += 1
            
        if hs.TrangthaiXetduyet == 0:
            total_hs_success +=1
        elif hs.TrangthaiXetduyet == 1:
            total_hs_unsuccess += 1   
        
    percent_hs_valid = round((total_hs_valid/total_hs) * 100, 2)
    percent_hs_invalid = round((total_hs_invalid/total_hs) * 100, 2)
    percent_hs_success = round((total_hs_success/total_hs) * 100, 2)
    percent_hs_unsuccess = round((total_hs_unsuccess/total_hs) * 100, 2)
    
    current_month = datetime.now().month
    count_hs_valid = 0
    count_hs_invalid = 0
    count_hs_success = 0
    count_hs_unsuccess = 0
    count_hs_with_month1 = 0
    count_hs_with_month2 = 0
    count_hs_with_month3 = 0
    count_hs_with_month4 = 0
    hs_valid = []
    hs_invalid = []
    hs_success = []
    hs_unsuccess = []
    months_to_check = []
    months_to_check_str = []

    # Tạo danh sách các giá trị của tháng cần kiểm tra
    months_to_check = [(current_month - i) % 12 or 12 for i in range(4)]
    # Chuyển đổi số tháng thành tên tháng (dạng chuỗi)
    months_to_check_str = [calendar.month_abbr[month] for month in months_to_check]
    month1, month2, month3, month4 = months_to_check_str
    print(months_to_check_str)
    
    for hs in hs_s:
        if calendar.month_abbr[hs.Ngaydangky.month] == month1:
            count_hs_with_month1 += 1
        elif calendar.month_abbr[hs.Ngaydangky.month] == month2:
            count_hs_with_month2 += 1
        elif calendar.month_abbr[hs.Ngaydangky.month] == month3:
            count_hs_with_month3 += 1
        elif calendar.month_abbr[hs.Ngaydangky.month] == month4:
            count_hs_with_month4 += 1
                
    count_hs_1 = 0
    for hs in hs_s:
        if calendar.month_abbr[hs.Ngaydangky.month] == month1:
            count_hs_1 += 1
    # Lặp qua các tháng cần kiểm tra
    for month in months_to_check:
        # Đặt lại các biến đếm
        count_hs_valid = 0
        count_hs_invalid = 0
        count_hs_success = 0
        count_hs_unsuccess = 0
        
        for hs in hs_s:
            if hs.Ngaydangky.month == month:
                if hs.TrangthaiXacnhan == 0:
                    count_hs_valid += 1
                elif hs.TrangthaiXacnhan == 1:
                    count_hs_invalid += 1
                elif hs.TrangthaiXetduyet == 0:
                    count_hs_success += 1
                elif hs.TrangthaiXetduyet == 1:
                    count_hs_unsuccess += 1
        
        hs_valid.append(count_hs_valid)
        hs_invalid.append(count_hs_invalid)
        hs_success.append(count_hs_success)
        hs_unsuccess.append(count_hs_unsuccess)
        
    hs_invalid1, hs_invalid2, hs_invalid3, hs_invalid4 = hs_invalid
        
    hs_valid1, hs_valid2, hs_valid3, hs_valid4 = hs_valid
    if hs_valid2 != 0:
        percent_hs_valid_in_month_with_last_month = "tăng gấp " + str(round((hs_valid1 / hs_valid2) * 100, 1)) + " so với tháng trước"
    else:
        percent_hs_valid_in_month_with_last_month = "Không có hồ sơ nào hợp lệ tháng trước đó"  # Hoặc một giá trị nào đó bạn thấy hợp lý
    
    hs_success1, hs_success2, hs_success3, hs_success4 = hs_success
    if hs_success2 != 0:
        percent_hs_success_in_month_with_last_month = "tăng gấp " + round((hs_success1 / hs_success2) * 100, 1) + " so với tháng trước"
    else:
        percent_hs_success_in_month_with_last_month = "Không có hồ sơ nào thành công tháng trước đó"  # Hoặc một giá trị nào đó bạn thấy hợp lý
        
    hs_unsuccess1, hs_unsuccess2, hs_unsuccess3, hs_unsuccess4 = hs_success
    if hs_unsuccess2 != 0:
        percent_hs_unsuccess_in_month_with_last_month = "tăng gấp " + round((hs_unsuccess1 / hs_unsuccess2) * 100, 1) + " so với tháng trước"
    else:
        percent_hs_unsuccess_in_month_with_last_month = "Không có hồ sơ nào thành công tháng trước đó"  # Hoặc một giá trị nào đó bạn thấy hợp lý
    
    if count_hs_with_month2 != 0:
        percent_hs_in_month_with_last_month = round((count_hs_with_month1 / count_hs_with_month2) * 100, 1)
    else:
        percent_hs_in_month_with_last_month = 0
       
    context = {
        'hs_s' : hs_s,
        'total_hs' : total_hs,
        'total_hs_valid' : total_hs_valid,
        'total_hs_invalid' : total_hs_invalid,
        'total_hs_success' : total_hs_success,
        'total_hs_unsuccess' : total_hs_unsuccess,
        'percent_hs_valid' : percent_hs_valid,
        'percent_hs_invalid' : percent_hs_invalid,
        'percent_hs_success' : percent_hs_success,
        'percent_hs_unsuccess' : percent_hs_unsuccess,
        'hs_objects' : hs_objects,
        'hs_valid' : hs_valid,
        'hs_invalid' : hs_invalid,
        'hs_success' : hs_success,
        'hs_unsuccess' : hs_unsuccess,
        'month1' : month1,
        'month2' : month2,
        'month3' : month3,
        'month4' : month4,
        'count_hs_with_month1' : count_hs_with_month1,
        'count_hs_with_month2' : count_hs_with_month2,
        'count_hs_with_month3' : count_hs_with_month3,
        'count_hs_with_month4' : count_hs_with_month4,
        'percent_hs_in_month_with_last_month' : percent_hs_in_month_with_last_month,
        'percent_hs_valid_in_month_with_last_month' : percent_hs_valid_in_month_with_last_month,
        'percent_hs_success_in_month_with_last_month' : percent_hs_success_in_month_with_last_month,
        'percent_hs_unsuccess_in_month_with_last_month' : percent_hs_unsuccess_in_month_with_last_month,
        'hs_unsuccess1' : hs_unsuccess1,
        'hs_valid1' : hs_valid1,
        'hs_success1' : hs_success1,
        'hs1' : count_hs_1,
    }
    
    return render(request, 'app/charts.html', context)

def status(request):
    # Đối tượng chính sách
    dtcs_s = DoiTuongChinhSach.objects.all()
    # Tiêu chí
    tcs = TieuChi.objects.all()

    total_dtcs = dtcs_s.count()
    
    # Cắt chuỗi đối tượng chính sách tại đây
    truncated_dtcs_s = []
    for dtcs in dtcs_s:
        # Giả sử bạn muốn cắt chuỗi ở thuộc tính 'name' và giới hạn ở 50 ký tự
        truncated_mota = dtcs.Mota[:50] + '...' if len(dtcs.Mota) > 50 else dtcs.Mota
        # Tạo một bản sao của đối tượng với tên đã được cắt ngắn
        truncated_dtcs_s.append({
            'MDT': dtcs.MDT,
            'Mota': truncated_mota,
            'Mucmiengiam' : dtcs.Mucmiengiam,
            'Thoigianhuong' : dtcs.Thoigianhuong,
            'MLDT_id' : dtcs.MLDT
            # Thêm các thuộc tính khác nếu cần
        })
        
    # Cắt chuỗi tiêu chí tại đây
    truncated_tc_s = []
    for tc in tcs:
        truncated_mota = tc.Mota[:50] + '...' if len(tc.Mota) > 50 else tc.Mota
        truncated_tc_s.append({
            'MTC' : tc.MTC,
            'Mota' : truncated_mota
        })

    context = {
        'dtcs_s': dtcs_s,
        'tc_s' : tcs,
        'total_dtcs': total_dtcs
    }
    
    return render(request, 'app/status.html', context)
    