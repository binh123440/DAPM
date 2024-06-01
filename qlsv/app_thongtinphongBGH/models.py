from django.db import models

class BanGiamHieu(models.Model):
    GIOI_TINH_CHOICES = [
        (0, 'Nam'),
        (1, 'Nữ'),
    ]  # Định nghĩa choices cho giới tính

    ROLES_CHOICES = [
        (0, 'Hiệu Trưởng'),
        (1, 'Hiệu Phó'),
    ]
    
    MNV = models.CharField(max_length=15, primary_key=True)
    Hoten = models.CharField(max_length=50)
    Ngaysinh = models.DateField(null=True, blank=True)  
    Gioitinh = models.IntegerField(choices=GIOI_TINH_CHOICES, default=0)
    SDT = models.CharField(max_length=12, null=True, blank=True)  
    Email = models.EmailField(null=True, blank=True)  
    Roles = models.IntegerField(choices=ROLES_CHOICES, null=False)
    Matkhau = models.CharField(max_length=50, null=False)
    Image = models.ImageField(upload_to='avt/%y', null=True, blank=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Roles'], condition=models.Q(Roles=0), name='unique_hieu_truong')
        ]    

    def __str__(self):
        return f"[{self.MNV}] - {self.Hoten}"
