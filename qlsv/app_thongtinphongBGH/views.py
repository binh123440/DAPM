from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import BanGiamHieu
from django.http import JsonResponse
from datetime import datetime

def thongtinphongBGH(request, MNV):
    bgh = get_object_or_404(BanGiamHieu, MNV=MNV)
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
        bgh.Matkhau = matkhau
        if image:
            bgh.Image = image
        bgh.save()

        return JsonResponse({'success': True, 'message': "Cập nhật thông tin thành công!"})

    context = {'bgh': bgh}
    return render(request, 'thongtinphongBGH.html', context)
    