# app_thongtinsinhvien/urls.py

from django.urls import path
from . import views  

urlpatterns = [
    path('', views.thongtinphongCTSV, name='thongtinphongCTSV'), 
    # ... các URL khác
]
