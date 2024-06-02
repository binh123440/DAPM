from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse
from django.http import JsonResponse
from collections import defaultdict
from datetime import datetime
from app.models import DoiTuongChinhSach, TieuChi, HoSoDangKy, DaiDienPhongBan, SinhVien
from app.forms import SinhVienForm, DaiDienPhongBanForm

# Create your views here.

def signin(request):
    if request.method == "GET":
        username_login = request.GET.get('username')
        password_login = request.GET.get('Pass')
        
        print(f"Username: {username_login}, Password: {password_login}")  # In ra giá trị để kiểm tra
        
        if username_login is None or password_login is None:
            return render(request, "signin.html")
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
    return render(request, "signin.html")
     
def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('signin')     
            
def signup(request):
    if request.method == 'POST':
        form = SinhVienForm(request.POST)
        if form.is_valid():
            msv = form.cleaned_data['MSV']
            hoten = form.cleaned_data['Hoten']
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Pass']
            
            request.session['username'] = form.cleaned_data['MSV']
            print(request.session['username'])
            
            # Tạo một instance mới của SinhVien và lưu vào cơ sở dữ liệu
            sinhvien = SinhVien(MSV=msv, Hoten=hoten, Email=email, Pass=password)
            sinhvien.save()
            # Chuyển hướng người dùng đến trang khác sau khi đăng ký thành công
            return redirect('base')  # Thay 'base' bằng tên của URLpattern bạn muốn chuyển hướng đến
    else:
        form = SinhVienForm()
        
    context = {
        'form' : form
    }
    
    return render(request, "signup.html", context)

def login(request):
    if request.method == 'POST':
        form = SinhVienForm(request.POST)
        if form.is_valid():
            msv = form.cleaned_data['MSV']
            hoten = form.cleaned_data['Hoten']
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Pass']
            
            request.session['username'] = form.cleaned_data['MSV']
            print(request.session['username'])
            
            # Tạo một instance mới của SinhVien và lưu vào cơ sở dữ liệu
            sinhvien = SinhVien(MSV=msv, Hoten=hoten, Email=email, Pass=password)
            sinhvien.save()
            # Chuyển hướng người dùng đến trang khác sau khi đăng ký thành công
            return redirect('base')  # Thay 'base' bằng tên của URLpattern bạn muốn chuyển hướng đến
    elif request.method == "GET":
        username_login = request.GET.get('username')
        password_login = request.GET.get('password')
        
        print(f"Username: {username_login}, Password: {password_login}")  # In ra giá trị để kiểm tra

        sinh_vien_s = SinhVien.objects.all()
        nhan_vien_s = DaiDienPhongBan.objects.all()
        
        if username_login is None or password_login is None:
            return render(request, "login.html")
        elif len(username_login) == 0:
            return HttpResponse("Username is required", status=400)
        elif len(username_login) <= 10:
            for nv in nhan_vien_s:
                if username_login == nv.MNV and password_login == nv.Pass:
                    if 'username' in request.session:
                        del request.session['username']
                    else:
                        request.session['username'] = nv.MNV
                    print(f"Nhan vien login: {request.session['username']}")
                    return redirect('base')  # Thay 'base' bằng tên của URLpattern bạn muốn chuyển hướng đến
        else:
            for sv in sinh_vien_s:
                if username_login == sv.MSV and password_login == sv.Pass:
                    request.session['username'] = sv.MSV
                    print(f"Sinh vien login: {request.session['username']}")
                    return redirect('base')  # Thay 'base' bằng tên của URLpattern bạn muốn chuyển hướng đến
                
    return render(request, "login.html")

def base(request):
    hs_s = HoSoDangKy.objects.all()
    total_hs = hs_s.count()
    
    username = request.session.get('username')
    print(username)
    
    if len(username) > 10:
        try:
            user = SinhVien.objects.get(MSV=username)
            print(f"Found nhan_vien: {user}")
        except SinhVien.DoesNotExist:
            print("Không có sinh viên có msv tồn tại")
        except SinhVien.MultipleObjectsReturned:
            print("Có nhiều hơn 1 sv tồn tại với msv")
    else:
        try:
            user = DaiDienPhongBan.objects.get(MNV=username)
            print(f"Found nhan_vien: {user}")
        except DaiDienPhongBan.DoesNotExist:
            print("Không có nhân viên có mnv tồn tại")
        except DaiDienPhongBan.MultipleObjectsReturned:
            print("Có nhiều hơn 1 nv tồn tại với mnv")
    
    hs_objects = []
    for hs in hs_s:
        sinh_vien = hs.MSV
        ten_sinh_vien = sinh_vien.Hoten
        trang_thai_xac_nhan = hs.TrangthaiXacnhan
        ngay_dang_ky = hs.Ngaydangky.date()
        thoi_gian_dang_ky = hs.Ngaydangky.time()
        nhan_vien = hs.MNV
        ten_nhan_vien = nhan_vien.Hoten
        ngay_xet_duyet = hs.Ngayxetduyet.date()
        thoi_gian_xet_duyet = hs.Ngayxetduyet.time() 
        trang_thai_xet_duyet = hs.TrangthaiXetduyet
        
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
        'username' : user
    }
    
    return render(request, 'base.html', context)
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
        ngay_xet_duyet = hs.Ngayxetduyet.date()
        thoi_gian_xet_duyet = hs.Ngayxetduyet.time() 
        trang_thai_xet_duyet = hs.TrangthaiXetduyet
        
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
    }
    
    return render(request, 'charts.html', context)

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
    
    return render(request, 'status.html', context)