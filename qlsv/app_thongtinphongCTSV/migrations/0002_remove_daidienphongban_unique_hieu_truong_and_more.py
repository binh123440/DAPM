# Generated by Django 5.0.4 on 2024-05-31 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_thongtinphongCTSV', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='daidienphongban',
            name='unique_hieu_truong',
        ),
        migrations.AddField(
            model_name='daidienphongban',
            name='Image',
            field=models.ImageField(null=True, upload_to='avt/%y'),
        ),
        migrations.AlterField(
            model_name='daidienphongban',
            name='Roles',
            field=models.IntegerField(choices=[(0, 'Trưởng phòng'), (1, 'Phó phòng'), (2, 'Nhân viên')]),
        ),
        migrations.AddConstraint(
            model_name='daidienphongban',
            constraint=models.UniqueConstraint(condition=models.Q(('Roles', 0)), fields=('Roles',), name='unique_truong_phong'),
        ),
    ]