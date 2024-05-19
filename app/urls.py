from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('index/<int:mbv>/', views.bai_viet_detail),
]