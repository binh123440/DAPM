from django.db import models

class HinhAnh(models.Model):
    MHA = models.BigAutoField(primary_key=True)
    TenHA = models.CharField(max_length=255)

class LoaiDoiTuongChinhSach(models.Model):
    MLDT = models.IntegerField(primary_key=True)
    Mota = models.TextField()

class DoiTuongChinhSach(models.Model):
    MDT = models.BigAutoField(primary_key=True)
    Mota = models.TextField()
    Mucmiengiam = models.BigIntegerField()
    Thoigianhuong = models.IntegerField()
    MLDT = models.ForeignKey(LoaiDoiTuongChinhSach, on_delete=models.CASCADE)

class TieuChi(models.Model):
    MTC = models.BigAutoField(primary_key=True)
    Mota = models.TextField()

class SinhVien(models.Model):
    MSV = models.CharField(max_length=15, primary_key=True)
    Hoten = models.CharField(max_length=50)
    Ngaysinh = models.DateField()
    Gioitinh = models.IntegerField()
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

class DaiDienPhongBan(models.Model):
    MNV = models.CharField(max_length=15, primary_key=True)
    Hoten = models.CharField(max_length=50)
    Ngaysinh = models.DateField(null=True, blank=True)
    Gioitinh = models.IntegerField(null=True, blank=True)
    SDT = models.CharField(max_length=12, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Roles = models.IntegerField()
    Pass = models.CharField(max_length=50)

class BaiViet(models.Model):
    MBV = models.BigAutoField(primary_key=True)
    Noidung = models.TextField()
    Ngaydang = models.DateTimeField()
    NgayhetHieuluc = models.DateTimeField()
    MNV = models.ForeignKey(DaiDienPhongBan, on_delete=models.CASCADE)

class HinhAnhBaiViet(models.Model):
    MHA = models.ForeignKey(HinhAnh, on_delete=models.CASCADE)
    MBV = models.ForeignKey(BaiViet, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('MHA', 'MBV')

class HoSoDangKy(models.Model):
    MHSDK = models.BigAutoField(primary_key=True)
    MSV = models.ForeignKey(SinhVien, on_delete=models.CASCADE)
    MNV = models.ForeignKey(DaiDienPhongBan, on_delete=models.CASCADE, null=True, blank=True)
    MotaHoancanhKhokhan = models.CharField(max_length=3000, null=True, blank=True)
    TrangthaiXacnhan = models.IntegerField(null=True, blank=True)
    Ngaydangky = models.DateTimeField(null=True, blank=True)
    Ngayxacnhan = models.DateTimeField(null=True, blank=True)
    TrangthaiXetduyet = models.IntegerField(null=True, blank=True)
    Ngayxetduyet = models.DateTimeField(null=True, blank=True)
    Hocki = models.CharField(max_length=3)
    MDT = models.ForeignKey(DoiTuongChinhSach, on_delete=models.CASCADE)

class ChiTietHoSo(models.Model):
    MHSDK = models.ForeignKey(HoSoDangKy, on_delete=models.CASCADE)
    MTC = models.ForeignKey(TieuChi, on_delete=models.CASCADE)
    MHA = models.ForeignKey(HinhAnh, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('MHSDK', 'MTC', 'MHA')

class QuyDinhApDung(models.Model):
    MBV = models.ForeignKey(BaiViet, on_delete=models.CASCADE)
    MDT = models.ForeignKey(DoiTuongChinhSach, on_delete=models.CASCADE)
    MTC = models.ForeignKey(TieuChi, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('MBV', 'MDT', 'MTC')
