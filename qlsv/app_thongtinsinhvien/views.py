from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SinhVien
from django.http import JsonResponse
from datetime import datetime

#def chinhsuathongtin(request, pk):
    #sinhvien = get_object_or_404(SinhVien, pk=pk)
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
        sinhvien.Matkhau = matkhau
        if image:
            sinhvien.Image = image
        sinhvien.save()
        return JsonResponse({'success': True, 'message': "Cập nhật thông tin thành công!"})
    else:
        context = {'sinhvien': sinhvien}
        return render(request, 'chinhsuathongtin.html', context)
    


