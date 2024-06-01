from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import PhongCTSV
from django.http import JsonResponse
from datetime import datetime

def thongtinphongCTSV(request, MNV):
    phongctvs = get_object_or_404(PhongCTSV, MNV=MNV)
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
        phongctvs.Matkhau = matkhau
        if image:
            phongctvs.Image = image
        phongctvs.save()

        return JsonResponse({'success': True, 'message': "Cập nhật thông tin thành công!"})

    context = {'phongctvs': phongctvs}
    return render(request, 'thongtinphongCTSV.html', context)
    