# Generated by Django 5.0.6 on 2024-05-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BaiViet', '0006_rename_ha_baiviet_anhbia_baiviet_tieude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baiviet',
            name='Ngaydang',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='baiviet',
            name='NgayhetHieuluc',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hosodangky',
            name='Ngaydangky',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hosodangky',
            name='Ngayxacnhan',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hosodangky',
            name='Ngayxetduyet',
            field=models.DateField(blank=True, null=True),
        ),
    ]
