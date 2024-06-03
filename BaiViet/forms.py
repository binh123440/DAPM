from django import forms

class SinhVienForm(forms.Form):
    MSV = forms.CharField(max_length=15)
    Hoten = forms.CharField(max_length=50)
    Email = forms.CharField(max_length=50)
    Pass = forms.CharField(max_length=50)
    
class DaiDienPhongBanForm(forms.Form):
    MNV = forms.CharField(max_length=15)
    Hoten = forms.CharField(max_length=50)
    Email = forms.CharField(max_length=50)
    Pass = forms.CharField(max_length=50)