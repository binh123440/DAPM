"""
URL configuration for test1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BaiViet import views as baiviet

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', baiviet.index, name='index'),
    path('index/<int:mbv>/', baiviet.detail, name='detail'),
    path('BaiViet/', baiviet.get_BaiViet , name="BaiViet"),
    path('DangKyHoSo/', baiviet.get_DangKyHoSo , name="DangKyHS"),
    path('load-more-posts/', baiviet.load_more_posts, name='load_more_posts'),
    path('luu-ho-so-dang-ky/', baiviet.luu_ho_so_dang_ky, name='luu-ho-so-dang-ky'),
    path('sinhvien/<str:MSV>/chinhsua', baiviet.chinhsuathongtin, name='chinhsuathongtin'), 
    path('phongCTSV/<str:MNV>/chinhsua', baiviet.thongtinphongCTSV, name='thongtinphongCTSV'), 
    path('phongBGH/<str:MNV>/chinhsua', baiviet.thongtinphongBGH, name='thongtinphongBGH'), 
    path('base/', baiviet.base, name="base"),
    path('charts/', baiviet.charts, name="charts"),
    path('status/', baiviet.status, name="status"),
    #path('login/', baiviet.login, name="login"),
    path('signin/', baiviet.signin, name="signin"),
    path('signup/', baiviet.signup, name="signup"),
    path('logout/', baiviet.logout, name="logout")
    

]
urlpatterns +=static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT)
