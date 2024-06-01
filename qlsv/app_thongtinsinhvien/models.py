from django.db import models

class SinhVien(models.Model):
    GIOI_TINH_CHOICES = [
        (0, 'Nam'),
        (1, 'Nữ'),
    ]  # Định nghĩa choices cho giới tính

    MSV = models.CharField(max_length=15, primary_key=True)
    Hoten = models.CharField(max_length=50)
    Ngaysinh = models.DateField()
    Gioitinh = models.IntegerField(choices=GIOI_TINH_CHOICES)  # Sử dụng choices
    CCCD = models.CharField(max_length=12)
    Quequan = models.CharField(max_length=255)
    SDT = models.CharField(max_length=12)
    Email = models.EmailField(unique=True)
    Lopsinhhoat = models.CharField(max_length=10)
    Nganhhoc = models.CharField(max_length=50)
    Khoa = models.CharField(max_length=50)
    Nienkhoa = models.CharField(max_length=9)
    Dantoc = models.CharField(max_length=255)
    Matkhau = models.CharField(max_length=50)  
    Image = models.ImageField(upload_to='avt/%y', null=True)

    def __str__(self):
        return f"[{self.MSV}] - {self.Hoten}"
