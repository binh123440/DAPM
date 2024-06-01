from django.db import models

class PhongCTSV(models.Model):
    GIOI_TINH_CHOICES = [
        (0, 'Nam'),
        (1, 'Nữ'),
    ]  # Định nghĩa choices cho giới tính

    ROLES_CHOICES = [
        (0, 'Trưởng phòng'),
        (1, 'Phó phòng'),
        (2, 'Nhân viên'),
    ]
    
    MNV = models.CharField(max_length=15, primary_key=True)
    Hoten = models.CharField(max_length=50)
    Ngaysinh = models.DateField()
    Gioitinh = models.IntegerField(choices=GIOI_TINH_CHOICES)  # Sử dụng choices
    SDT = models.CharField(max_length=12)
    Email = models.EmailField(unique=True)
    Roles = models.IntegerField(choices=ROLES_CHOICES)
    Matkhau = models.CharField(max_length=50)  
    Image = models.ImageField(upload_to='avt/%y', null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['Roles'], condition=models.Q(Roles=0), name='unique_truong_phong')
        ]    

    def __str__(self):
        return f"[{self.MNV}] - {self.Hoten}"
