# app_thongtinsinhvien/urls.py

from django.urls import path
from . import views  # Đảm bảo import đúng cách

urlpatterns = [
    path('', views.thongtinphongBGH, name='thongtinphongBGH'), 
    # ... các URL khác
]
