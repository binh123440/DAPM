# app_thongtinsinhvien/urls.py

from django.urls import path
from . import views  # Đảm bảo import đúng cách

urlpatterns = [
    path('', views.thongtinphongCTSV, name='thongtinphongCTSV'), 
    # ... các URL khác
]
