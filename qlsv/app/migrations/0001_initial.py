# Generated by Django 4.2.13 on 2024-05-28 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DaiDienPhongBan',
            fields=[
                ('MNV', models.CharField(blank=True, max_length=15, primary_key=True, serialize=False)),
                ('Hoten', models.CharField(blank=True, max_length=50)),
                ('Ngaysinh', models.DateField(blank=True)),
                ('Gioitinh', models.IntegerField(blank=True)),
                ('SDT', models.CharField(blank=True, max_length=12)),
                ('Email', models.CharField(blank=True, max_length=50)),
                ('Roles', models.IntegerField(blank=True)),
                ('Pass', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'db_table': 'DaiDienPhongBan',
            },
        ),
        migrations.CreateModel(
            name='DoiTuongChinhSach',
            fields=[
                ('MDT', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Mota', models.CharField(blank=True, max_length=2000)),
                ('Mucmiengiam', models.BigIntegerField(blank=True)),
                ('Thoigianhuong', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'DoiTuongChinhSach',
            },
        ),
        migrations.CreateModel(
            name='HinhAnh',
            fields=[
                ('MHA', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('TenHA', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'db_table': 'HinhAnh',
            },
        ),
        migrations.CreateModel(
            name='LoaiDoiTuongChinhSach',
            fields=[
                ('MLDT', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Mota', models.CharField(blank=True, max_length=2000)),
            ],
            options={
                'db_table': 'LoaiDoiTuongChinhSach',
            },
        ),
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('MSV', models.CharField(blank=True, max_length=15, primary_key=True, serialize=False)),
                ('Hoten', models.CharField(blank=True, max_length=50)),
                ('Ngaysinh', models.DateField(blank=True)),
                ('Gioitinh', models.IntegerField(blank=True)),
                ('CCCD', models.CharField(blank=True, max_length=12)),
                ('Quequan', models.CharField(blank=True, max_length=255)),
                ('SDT', models.CharField(blank=True, max_length=12)),
                ('Email', models.CharField(blank=True, max_length=50)),
                ('Lopsinhhoat', models.CharField(blank=True, max_length=10)),
                ('Nganhhoc', models.CharField(blank=True, max_length=50)),
                ('Khoa', models.CharField(blank=True, max_length=50)),
                ('Nienkhoa', models.CharField(blank=True, max_length=9)),
                ('Dantoc', models.CharField(blank=True, max_length=255)),
                ('Pass', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'db_table': 'SinhVien',
            },
        ),
        migrations.CreateModel(
            name='TieuChi',
            fields=[
                ('MTC', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Mota', models.CharField(blank=True, max_length=2000)),
            ],
            options={
                'db_table': 'TieuChi',
            },
        ),
        migrations.CreateModel(
            name='HoSoDangKy',
            fields=[
                ('MHSDK', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('MotaHoancanhKhokhan', models.CharField(blank=True, max_length=5000)),
                ('TrangthaiXacnhan', models.IntegerField(blank=True)),
                ('Ngaydangky', models.DateTimeField(blank=True)),
                ('Ngayxacnhan', models.DateTimeField(blank=True)),
                ('TrangthaiXetduyet', models.IntegerField(blank=True)),
                ('Ngayxetduyet', models.DateTimeField(blank=True)),
                ('Hocki', models.CharField(blank=True, max_length=3)),
                ('MDT', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.doituongchinhsach')),
                ('MNV', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.daidienphongban')),
                ('MSV', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.sinhvien')),
            ],
            options={
                'db_table': 'HoSoDangKy',
            },
        ),
        migrations.AddField(
            model_name='doituongchinhsach',
            name='MLDT',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.loaidoituongchinhsach'),
        ),
        migrations.CreateModel(
            name='BaiViet',
            fields=[
                ('MBV', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Noidung', models.CharField(blank=True, max_length=5000)),
                ('Ngaydang', models.DateTimeField(blank=True)),
                ('NgayhetHieuluc', models.DateTimeField(blank=True)),
                ('MNV', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.daidienphongban')),
            ],
            options={
                'db_table': 'BaiViet',
            },
        ),
        migrations.CreateModel(
            name='QuyDinhApDung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MBV', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.baiviet')),
                ('MDT', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.doituongchinhsach')),
                ('MTC', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.tieuchi')),
            ],
            options={
                'db_table': 'QuyDinhApDung',
                'unique_together': {('MBV', 'MDT', 'MTC')},
            },
        ),
        migrations.CreateModel(
            name='HinhAnhBaiViet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MBV', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.baiviet')),
                ('MHA', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.hinhanh')),
            ],
            options={
                'db_table': 'HinhAnhBaiViet',
                'unique_together': {('MHA', 'MBV')},
            },
        ),
        migrations.CreateModel(
            name='ChiTietHoSo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MHA', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.hinhanh')),
                ('MHSDK', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.hosodangky')),
                ('MTC', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.tieuchi')),
            ],
            options={
                'db_table': 'ChiTietHoSo',
                'unique_together': {('MHSDK', 'MTC', 'MHA')},
            },
        ),
    ]
