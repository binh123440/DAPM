# Generated by Django 4.2.13 on 2024-06-01 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaiViet', '0011_daidienphongban_image_alter_daidienphongban_gioitinh_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sinhvien',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sinhvien',
            name='Gioitinh',
            field=models.IntegerField(blank=True, choices=[(0, 'Nam'), (1, 'Nữ')], null=True),
        ),
    ]
