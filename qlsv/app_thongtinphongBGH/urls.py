# app_thongtinsinhvien/urls.py

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.thongtinphongBGH, name='thongtinphongBGH'), 
    # ... các URL khác
]
