import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse
from django.http import JsonResponse
from collections import defaultdict
from django.utils import timezone

# datetime
from datetime import datetime
import pytz
import calendar
from django.conf import settings
# Thiết lập múi giờ cho Hồ Chí Minh
ho_chi_minh_tz = pytz.timezone('Asia/Ho_Chi_Minh')

from app.models import DoiTuongChinhSach, TieuChi, HoSoDangKy, DaiDienPhongBan, SinhVien
from app.forms import SinhVienForm, DaiDienPhongBanForm

# Create your views here.

def get_current_hcm_time():
    # Lấy múi giờ của Hồ Chí Minh
    hcm_tz = pytz.timezone('Asia/Ho_Chi_Minh')
    
    # Lấy thời gian hiện tại theo múi giờ UTC
    utc_now = datetime.now(pytz.utc)
    
    # Chuyển đổi thời gian hiện tại về múi giờ Hồ Chí Minh
    hcm_now = utc_now.astimezone(hcm_tz)
    
    return hcm_now

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
    return render(request, 'view_detail.html', context)

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
        mahs = hs.MHSDK
        sinh_vien = hs.MSV
        ten_sinh_vien = sinh_vien.Hoten
        trang_thai_xac_nhan = hs.TrangthaiXacnhan
        ngay_dang_ky = hs.Ngaydangky.date()
        thoi_gian_dang_ky = hs.Ngaydangky.time()
        nhan_vien = hs.MNV
        ten_nhan_vien = nhan_vien.Hoten
        if hs.Ngayxetduyet is None:
            ngay_xet_duyet = ""
            thoi_gian_xet_duyet = ""
        else:
            ngay_xet_duyet = hs.Ngayxetduyet.date()
            thoi_gian_xet_duyet = hs.Ngayxetduyet.time() 
        trang_thai_xet_duyet = hs.TrangthaiXetduyet
        
        hs_objects.append({
            'MaHS' : mahs,
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
      
    percent_hs_in_month_with_last_month = round((count_hs_with_month1 / count_hs_with_month2) * 100, 1)
      
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
      
    percent_hs_in_month_with_last_month = round((count_hs_with_month1 / count_hs_with_month2) * 100, 1)
       
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