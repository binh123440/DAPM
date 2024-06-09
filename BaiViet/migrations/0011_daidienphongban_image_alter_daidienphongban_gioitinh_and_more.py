# Generated by Django 4.2.13 on 2024-06-01 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaiViet', '0010_hosodangky_mdt_alter_quydinhapdung_mdt'),
    ]

    operations = [
        migrations.AddField(
            model_name='daidienphongban',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='daidienphongban',
            name='Gioitinh',
            field=models.IntegerField(blank=True, choices=[(0, 'Nam'), (1, 'Nữ')], null=True),
        ),
        migrations.AlterField(
            model_name='daidienphongban',
            name='Roles',
            field=models.IntegerField(choices=[(0, 'Trưởng phòng'), (1, 'Phó phòng'), (2, 'Nhân viên'), (3, 'Hiệu Trưởng'), (4, 'Hiệu Phó')]),
        ),
    ]
