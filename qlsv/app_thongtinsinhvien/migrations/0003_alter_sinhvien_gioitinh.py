# Generated by Django 5.0.4 on 2024-05-29 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_thongtinsinhvien', '0002_alter_sinhvien_gioitinh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sinhvien',
            name='Gioitinh',
            field=models.IntegerField(choices=[(0, 'Nam'), (1, 'Nữ')]),
        ),
    ]
