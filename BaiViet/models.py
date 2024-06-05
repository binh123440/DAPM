from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models

class LoaiDoiTuongChinhSach(models.Model):
    MLDT = models.IntegerField(primary_key=True)
    Mota = models.TextField()

# Tạo danh sách đối tượng cho LoaiDoiTuongChinhSach



class DoiTuongChinhSach(models.Model):
    MDT = models.AutoField(primary_key=True)
    Mota = models.TextField()
    Mucmiengiam = models.BigIntegerField()
    Thoigianhuong = models.IntegerField()
    MLDT = models.ForeignKey(LoaiDoiTuongChinhSach, on_delete=models.CASCADE, related_name='doituongchinhsach')




class TieuChi(models.Model):
    MTC = models.AutoField(primary_key=True)
    Mota = models.TextField()

class SinhVien(models.Model):
    GIOI_TINH_CHOICES = [
        (0, 'Nam'),
        (1, 'Nữ'),
    ]  # Định nghĩa choices cho giới tính
    MSV = models.CharField(max_length=15, primary_key=True)
    Hoten = models.CharField(max_length=50)
    Ngaysinh = models.DateField()
    Gioitinh = models.IntegerField(choices=GIOI_TINH_CHOICES, null=True, blank=True)  # 0: Nam, 1: Nữ
    CCCD = models.CharField(max_length=12)
    Quequan = models.CharField(max_length=255)
    SDT = models.CharField(max_length=12, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Lopsinhhoat = models.CharField(max_length=10)
    Nganhhoc = models.CharField(max_length=50)
    Khoa = models.CharField(max_length=50)
    Nienkhoa = models.CharField(max_length=9)
    Dantoc = models.CharField(max_length=255)
    Pass = models.CharField(max_length=50)
    Image = models.ImageField( null=True, blank=True)

class HinhAnh(models.Model):
    MHA = models.AutoField(primary_key=True)
    TenHA = models.CharField(max_length=255)
    HA = models.ImageField()

class DaiDienPhongBan(models.Model):
    GIOI_TINH_CHOICES = [
        (0, 'Nam'),
        (1, 'Nữ'),
    ]  # Định nghĩa choices cho giới tính

    ROLES_CHOICES = [
        (0, 'Trưởng phòng'),
        (1, 'Phó phòng'),
        (2, 'Nhân viên'),
        (3, 'Hiệu Trưởng'),
        (4, 'Hiệu Phó'),
    ]
    MNV = models.CharField(max_length=15, primary_key=True)
    Hoten = models.CharField(max_length=50)
    Ngaysinh = models.DateField(null=True, blank=True)
    Gioitinh = models.IntegerField(choices=GIOI_TINH_CHOICES, null=True, blank=True)
    SDT = models.CharField(max_length=12, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Roles = models.IntegerField(choices=ROLES_CHOICES) 
    Pass = models.CharField(max_length=50)
    Image = models.ImageField(null=True, blank=True)

class BaiViet(models.Model):
    MBV = models.AutoField(primary_key=True)
    Noidung = models.TextField()
    TieuDe = models.TextField(null=True, blank=True)
    Ngaydang = models.DateField()
    NgayhetHieuluc = models.DateField()
    MNV = models.ForeignKey(DaiDienPhongBan, on_delete=models.CASCADE, related_name='baiviet')
    AnhBia = models.ImageField(null=True, blank=True)

class HinhAnhBaiViet(models.Model):
    MHA = models.ForeignKey(HinhAnh, on_delete=models.CASCADE)
    MBV = models.ForeignKey(BaiViet, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('MHA', 'MBV')

class HoSoDangKy(models.Model):
    MHSDK = models.AutoField(primary_key=True)
    MSV = models.ForeignKey(SinhVien, on_delete=models.CASCADE, related_name='hosodangky')
    MNV = models.ForeignKey(DaiDienPhongBan, on_delete=models.CASCADE, null=True, blank=True, related_name='hosodangky')
    MotaHoancanhKhokhan = models.CharField(max_length=3000)
    TrangthaiXacnhan = models.IntegerField()
    Ngaydangky = models.DateTimeField()
    Ngayxacnhan = models.DateTimeField(null=True, blank=True)
    TrangthaiXetduyet = models.IntegerField(null=True, blank=True)
    Ngayxetduyet = models.DateTimeField(null=True, blank=True)
    Hocki = models.CharField(max_length=3)
    MDT = models.ForeignKey(DoiTuongChinhSach, on_delete=models.CASCADE, related_name='hosodangky', null=True, blank=True)

class ChiTietHoSo(models.Model):
    MHSDK = models.ForeignKey(HoSoDangKy, on_delete=models.CASCADE)
    MTC = models.ForeignKey(TieuChi, on_delete=models.CASCADE, null=True, blank=True)
    MHA = models.ForeignKey(HinhAnh, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('MHSDK', 'MTC', 'MHA')

class QuyDinhApDung(models.Model):
    MBV = models.ForeignKey(BaiViet, on_delete=models.CASCADE)
    MDT = models.ForeignKey(DoiTuongChinhSach, on_delete=models.CASCADE, null=True, blank=True)
    MTC = models.ForeignKey(TieuChi, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('MBV', 'MDT', 'MTC')

        