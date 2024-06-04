from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
# Create your models here.

# Null = true, tức là những ô ko chứa dữ liệu sẽ hiển thị là "NULL"
# Blank = False, tức là dữ liệu bắt buộc phải có, ngược lại True là có thể không

from django.db import models

# Hình ảnh
class HinhAnh(models.Model):
    MHA = models.BigAutoField(auto_created=True, primary_key=True)
    TenHA = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "HinhAnh"
        
# Loại đối tượng chính sách
class LoaiDoiTuongChinhSach(models.Model):
    MLDT = models.BigAutoField(primary_key=True, auto_created=True, blank=True)
    Mota = models.CharField(max_length=2000, blank=True)

    class Meta:
        db_table = "LoaiDoiTuongChinhSach"

# Đối tượng chính sách
class DoiTuongChinhSach(models.Model):
    MDT = models.BigAutoField(auto_created=True, primary_key=True)
    Mota = models.CharField(max_length=2000, blank=True)
    Mucmiengiam = models.BigIntegerField(blank=True)
    Thoigianhuong = models.IntegerField(blank=True)
    MLDT = models.ForeignKey(LoaiDoiTuongChinhSach, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "DoiTuongChinhSach"

# Tiêu chí
class TieuChi(models.Model):
    MTC = models.BigAutoField(auto_created=True, primary_key=True)
    Mota = models.CharField(max_length=2000, blank=True)

    class Meta:
        db_table = "TieuChi"

# Sinh viên
class SinhVien(models.Model):
    MSV = models.CharField(max_length=15, primary_key=True, blank=True)
    Hoten = models.CharField(max_length=50, blank=True)
    Ngaysinh = models.DateField(blank=True, null=True)
    Gioitinh = models.IntegerField(blank=True, null=True)
    CCCD = models.CharField(max_length=12, blank=True, null=True)
    Quequan = models.CharField(max_length=255, blank=True, null=True)
    SDT = models.CharField(max_length=12, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True)
    Lopsinhhoat = models.CharField(max_length=10, blank=True, null=True)
    Nganhhoc = models.CharField(max_length=50, blank=True, null=True)
    Khoa = models.CharField(max_length=50, blank=True, null=True)
    Nienkhoa = models.CharField(max_length=9, blank=True, null=True)
    Dantoc = models.CharField(max_length=255, blank=True, null=True)
    Pass = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = "SinhVien"

# Đại diện phòng ban
class DaiDienPhongBan(models.Model):
    MNV = models.CharField(max_length=15, primary_key=True, blank=True)
    Hoten = models.CharField(max_length=50, blank=True)
    Ngaysinh = models.DateField(blank=True)
    Gioitinh = models.IntegerField(blank=True)
    SDT = models.CharField(max_length=12, blank=True)
    Email = models.CharField(max_length=50, blank=True)
    Roles = models.IntegerField(null=False, blank=True)
    Pass = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = "DaiDienPhongBan"

# Bài viết
class BaiViet(models.Model):
    MBV = models.BigAutoField(auto_created=True, primary_key=True)
    Noidung = models.CharField(max_length=5000, blank=True)
    Ngaydang = models.DateTimeField(blank=True)
    NgayhetHieuluc = models.DateTimeField(blank=True)
    MNV = models.ForeignKey(DaiDienPhongBan, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "BaiViet"

# Hình ảnh bài viết
class HinhAnhBaiViet(models.Model):
    MHA = models.ForeignKey(HinhAnh, on_delete=models.CASCADE, blank=True)
    MBV = models.ForeignKey(BaiViet, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "HinhAnhBaiViet"
        unique_together = (('MHA', 'MBV'),)
        
# Hồ sơ đăng ký
class HoSoDangKy(models.Model):
    MHSDK = models.BigAutoField(auto_created=True, primary_key=True)
    MSV = models.ForeignKey(SinhVien, on_delete=models.CASCADE, blank=True)
    MNV = models.ForeignKey(DaiDienPhongBan, on_delete=models.CASCADE, blank=True)
    MotaHoancanhKhokhan = models.CharField(max_length=5000, blank=True)
    TrangthaiXacnhan = models.IntegerField(blank=True)
    Ngaydangky = models.DateTimeField(blank=True)
    Ngayxacnhan = models.DateTimeField(blank=True)
    TrangthaiXetduyet = models.IntegerField(blank=True)
    Ngayxetduyet = models.DateTimeField(blank=True)
    Hocki = models.CharField(max_length=3, blank=True)
    MDT = models.ForeignKey(DoiTuongChinhSach, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "HoSoDangKy"

# Chi tiết hồ sơ
class ChiTietHoSo(models.Model):
    MHSDK = models.ForeignKey(HoSoDangKy, on_delete=models.CASCADE, blank=True)
    MTC = models.ForeignKey(TieuChi, on_delete=models.CASCADE, blank=True)
    MHA = models.ForeignKey(HinhAnh, on_delete=models.CASCADE, blank=True)

    class Meta:
        db_table = "ChiTietHoSo"
        unique_together = (('MHSDK', 'MTC', 'MHA'),)

# Quy định áp dụng
class QuyDinhApDung(models.Model):
    MBV = models.ForeignKey(BaiViet, on_delete=models.CASCADE,blank=True)
    MDT = models.ForeignKey(DoiTuongChinhSach, on_delete=models.CASCADE,blank=True)
    MTC = models.ForeignKey(TieuChi, on_delete=models.CASCADE,blank=True)

    class Meta:
        db_table = "QuyDinhApDung"
        unique_together = (('MBV', 'MDT', 'MTC'),)
        
# loai_doi_tuong_data = [
#     {"Mota": "Đối tượng được miễn giảm học phí"},
#     {"Mota": "Đối tượng được nhận trợ cấp xã hội"},
#     {"Mota": "Đối tượng được nhận hỗ trợ chi phí học tập"},
# ]

# for ldt in loai_doi_tuong_data:
#     loai_doi_tuong = LoaiDoiTuongChinhSach(**ldt)  # Sử dụng unpack operator để truyền dữ liệu vào instance
#     loai_doi_tuong.save()
    
# doi_tuong_data = [
#     {"Mota": "Anh hùng LLVT nhân dân; thương binh; bệnh binh; người hưởng chế độ chính sách như thương binh (Ký hiệu: AH; TB; BB)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Con của người hoạt động cách mạng trước ngày 01/01/1945; con của người hoạt động cách mạng từ ngày 01/01/1945 đến trước Tổng khởi nghĩa 19/8/1945 (Ký hiệu: CCBCM)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Con của anh hùng lực lượng vũ trang nhân dân (Ký hiệu: CAH)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Con của anh hùng lao động trong thời kỳ kháng chiến (Ký hiệu: CAH)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Con của liệt sỹ (Ký hiệu: CLS)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Con của thương binh (Ký hiệu: CTB)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Con của bệnh binh (Ký hiệu: CBB)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Con của người hưởng chính sách như thương binh (Ký hiệu: CNTB)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Con của người hoạt động kháng chiến bị nhiễm chất độc hoá học (Ký hiệu: CĐHH)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Sinh viên từ 16 tuổi đến 22 tuổi đang học giáo dục đại học văn bằng thứ nhất thuộc đối tượng hưởng trợ cấp xã hội hàng tháng theo quy định tại khoản 1 và khoản 2 Điều 5 Nghị định số 20/2021/NĐ-CP ngày 15 tháng 3 năm 2021 của Chính phủ về chính sách trợ giúp xã hội đối với đối tượng bảo trợ xã hội thuộc một trong các trường hợp (Ký hiệu: MOCOI):\n+ Bị bỏ rơi chưa có người nhận làm con nuôi.\n+ Mồ côi cả cha và mẹ.\n+ Mồ côi cha hoặc mẹ và người còn lại bị tuyên bố mất tích theo quy định của pháp luật.\n+ Mồ côi cha hoặc mẹ và người còn lại đang hưởng chế độ chăm sóc, nuôi dưỡng tại cơ sở trợ giúp xã hội, nhà xã hội.\n+ Mồ côi cha hoặc mẹ và người còn lại đang trong thời gian chấp hành án phạt tù tại trại giam hoặc đang chấp hành quyết định xử lý vi phạm hành chính tại trường giáo dưỡng, cơ sở giáo dục bắt buộc, cơ sở cai nghiện bắt buộc.\n+ Cả cha và mẹ bị tuyên bố mất tích theo quy định của pháp luật.\n+ Cả cha và mẹ đang hưởng chế độ chăm sóc, nuôi dưỡng tại cơ sở trợ giúp xã hội, nhà xã hội.\n+ Cả cha và mẹ đang trong thời gian chấp hành án phạt tù tại trại giam hoặc đang chấp hành quyết định xử lý vi phạm hành chính tại trường giáo dưỡng, cơ sở giáo dục bắt buộc, cơ sở cai nghiện bắt buộc.\n+ Cha hoặc mẹ bị tuyên bố mất tích theo quy định của pháp luật và người còn lại đang hưởng chế độ chăm sóc, nuôi dưỡng tại cơ sở trợ giúp xã hội, nhà xã hội.\n+ Cha hoặc mẹ bị tuyên bố mất tích theo quy định của pháp luật và người còn lại đang trong thời gian chấp hành án phạt tù tại trại giam hoặc đang chấp hành quyết định xử lý vi phạm hành chính tại trường giáo dưỡng, cơ sở giáo dục bắt buộc, cơ sở cai nghiện bắt buộc.\n+ Cha hoặc mẹ đang hưởng chế độ chăm sóc, nuôi dưỡng tại cơ sở trợ giúp xã hội và người còn lại đang trong thời gian chấp hành án phạt tù tại trại giam hoặc đang chấp hành quyết định xử lý vi phạm hành chính tại trường giáo dưỡng, cơ sở giáo dục bắt buộc, cơ sở cai nghiện bắt buộc.", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Sinh viên là người dân tộc thiểu số rất ít người (La Hủ, La Ha, Pà Thẻn, Lự, Ngái, Chứt, Lô Lô, Mảng, Cống, Cờ Lao, Bố Y, Si La, Pu Péo, Rơ Măm, BRâu, Ơ Đu) ở vùng có điều kiện kinh tế - xã hội khó khăn hoặc đặc biệt khó khan (Ký hiệu: DT-09)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Sinh viên khuyết tật (Ký hiệu: TT)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Sinh viên hệ cử tuyển (Ký hiệu: CT)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Sinh viên là người dân tộc thiểu số có cha hoặc mẹ hoặc cả cha và mẹ hoặc ông bà (trong trường hợp ở với ông bà) thuộc hộ nghèo hoặc cận nghèo (Ký hiệu: DT-HN hoặc DT-HCN)", "Mucmiengiam": 100, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Sinh viên là người dân tộc thiểu số (không phải là dân tộc thiểu số rất ít người) ở thôn/bản đặc biệt khó khăn, xã khu vực III vùng dân tộc và miền núi, xã đặc biệt khó khăn vùng bãi ngang ven biển hải đảo theo quy định của cơ quan có thẩm quyền (Ký hiệu: DT-ĐBKK)", "Mucmiengiam": 70, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Sinh viên là con cán bộ, công nhân, viên chức mà cha hoặc mẹ bị tai nạn lao động hoặc mắc bệnh nghề nghiệp được hưởng trợ cấp thường xuyên (Ký hiệu: TNLĐ)", "Mucmiengiam": 50, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Sinh viên là con cán bộ, công chức, viên chức đang công tác tại Đại học Đà Nẵng", "Mucmiengiam": 50, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Sinh viên là con cán bộ, công chức, viên chức công tác tại Đại học Đà Nẵng đã nghỉ hưu theo chế độ", "Mucmiengiam": 25, "Thoigianhuong": 0, "MLDT": 1},
#     {"Mota": "Sinh viên là người dân tộc ít người ở vùng cao (có hộ khẩu thường trú tại địa phương từ 03 năm trở lên).", "Mucmiengiam": 140000, "Thoigianhuong": 12, "MLDT": 2},
#     {"Mota": "Sinh viên là người mồ coi cả cha lẫn mẹ không nơi nương tựa.", "Mucmiengiam": 100000, "Thoigianhuong": 12, "MLDT": 2},
#     {"Mota": "Sinh viên là người tàn tật, khuyết tật gặp khó khăn về kinh tế, khả năng lao động bị suy giảm từ 41% trở lên do tàn tật, được Hội đồng y khoa có thẩm quyền xác nhận.", "Mucmiengiam": 100000, "Thoigianhuong": 12, "MLDT": 2},
#     {"Mota": "Sinh viên có hoàn cảnh đặc biệt khó khăn về kinh tế, vượt khó học tập là những người mà gia đình của họ thuộc diện hộ nghèo.", "Mucmiengiam": 100000, "Thoigianhuong": 12, "MLDT": 2},
#     {"Mota": "Sinh viên là người dân tộc thiểu số thuộc hộ nghèo hoặc hộ cận nghèo.", "Mucmiengiam": 60, "Thoigianhuong": 10, "MLDT": 3},
#     {"Mota": "Sinh viên thuộc 16 dân tộc dân tộc thiểu số rất ít người (có số dân dưới 10.000 người: Cống, Mảng, Pu Péo, Si La, Cờ Lao, Bố Y, La Ha, Ngái, Chứt, Ơ Đu, Brâu, Rơ Măm, Lô Lô, Lự, Pà Thẻn, La Hù.", "Mucmiengiam": 60, "Thoigianhuong": 10, "MLDT": 3},
# ]
    
    
# doi_tuong_chinh_sach_objects = []
# for dt in doi_tuong_data:
#     dt['MLDT'] = LoaiDoiTuongChinhSach.objects.get(pk=dt['MLDT'])  # Ensure correct foreign key assignment
#     doi_tuong = DoiTuongChinhSach(**dt)
#     doi_tuong_chinh_sach_objects.append(doi_tuong)

# DoiTuongChinhSach.objects.bulk_create(doi_tuong_chinh_sach_objects)

# tieu_chi_data = [
#     {"Mota": "Giấy xác nhận là con của liệt sỹ, thương binh, bệnh binh, người hưởng chính sách như thương binh, bệnh binh do Phòng Lao động Thương binh."},
#     {"Mota": "Giấy xã hội cấp huyện cấp; Là con của người hoạt động kháng chiến bị nhiễm chất độc hóa học do Sở Lao động Thương binh - Xã hội cấp."},
#     {"Mota": "Bản sao chứng thực sao y bản chính Thẻ liệt sỹ, thương binh, bệnh binh, người hưởng chính sách như thương binh, bệnh binh hoặc quyết định hưởng trợ cấp hàng tháng của Sở LĐTB&XH; Biên bản giám định khả năng lao động do Hội đồng Y khoa cấp tỉnh, thành phố giám định hoặc các loại giấy tờ sau đây: Quyết định về việc trợ cấp đối với người hoạt động kháng chiến bị nhiễm chất độc hóa học do Sở Lao động Thương binh."},
#     {"Mota": "Giấy xã hội cấp; Quyết định về việc trợ cấp đối với con đẻ của người hoạt động kháng chiến bị nhiễm chất độc hóa học do Sở Lao động Thương binh."},
#     {"Mota": "Giấy xã hội cấp; - Bản sao chứng thực sao y bản chính Giấy khai sinh hoặc sổ hộ khẩu (có đầy đủ chữ ký, ngày tháng năm và số vào sổ chứng thực, sổ hộ khẩu cần có dấu tròn giáp lai ở tất cả các trang và được chứng thực trong vòng 6 tháng tính đến ngày nộp)."},
#     {"Mota": "Giấy xác nhận khuyết tật do Ủy ban nhân dân cấp xã cấp hoặc Quyết định về việc trợ cấp xã hội của Ủy ban nhân dân cấp huyện."},
#     {"Mota": "Bản sao chứng thực sao y bản chính Sổ hộ nghèo hoặc hộ cận nghèo do Ủy ban nhân dân xã cấp (có đầy đủ chữ ký, ngày tháng năm và số vào sổ chứng thực)"},
#     {"Mota": "Bản sao chứng thực sao y bản chính Sổ hộ khẩu (có đầy đủ chữ ký, ngày tháng năm và số vào sổ chứng thực, có dấu tròn giáp lai ở tất cả các trang và được chứng thực trong vòng 6 tháng tính đến ngày nộp)."},
#     {"Mota": "Giấy xác nhận là sinh viên mồ côi cả cha lẫn mẹ do UBND cấp xã cấp; hoặc văn bản xác nhận của công an cấp xã (nếu cha mẹ đang chịu án phạt tù…)."},
#     {"Mota": "Bản sao chứng thực sao y bản chính Quyết định hưởng trợ cấp xã hội hàng tháng theo nghị định 136/2013/NĐ-CP (có đầy đủ chữ ký, ngày tháng năm và số vào sổ chứng thực)."},
#     {"Mota": "Bản sao chứng thực sao y bản chính giấy khai sinh hoặc sổ hộ khẩu (có đầy đủ chữ ký, ngày tháng năm và số vào sổ chứng thực, sổ hộ khẩu cần có dấu tròn giáp lai ở tất cả các trang và được chứng thực trong vòng 6 tháng tính đến ngày nộp)."},
#     {"Mota": "Bản sao chứng thực sao y bản chính giấy khai sinh và sổ hộ khẩu (có đầy đủ chữ ký, ngày tháng năm và số vào sổ chứng thực, sổ hộ khẩu cần có dấu tròn giáp lai ở tất cả các trang và được chứng thực trong vòng 6 tháng tính đến ngày nộp) hoặc giấy đăng ký tạm trú."},
#     {"Mota": "Bản sao chứng thực sao y bản chính Sổ hưởng trợ cấp hàng tháng của cha hoặc mẹ bị tai nạn lao động hoặc mắc bệnh nghề nghiệp do tổ chức bảo hiểm xã hội cấp (có đầy đủ chữ ký, ngày tháng năm và số vào sổ chứng thực, có dấu giáp lai ở tất cả các trang nếu có nhiều hơn 1 trang)."},
#     {"Mota": "Bản sao chứng thực sao y bản chính Giấy khai sinh hoặc sổ hộ khẩu (có đầy đủ chữ ký, ngày tháng năm và số vào sổ chứng thực, sổ hộ khẩu cần có dấu tròn giáp lai ở tất cả các trang và được chứng thực trong vòng 6 tháng tính đến ngày nộp)."},
#     {"Mota": "Giấy chứng nhận UBND xã/phường/thị trấn về thời gian cư trú của SV."},
#     {"Mota": "Bản sao quyết định xã khó khăn."},
#     {"Mota": "Thư giới thiệu của phường xã"},
# ]

# for tc in tieu_chi_data:
#     tieu_chi = TieuChi(**tc)
#     tieu_chi.save()

# sinh_vien_data = [
#     {"MSV": "21115053120128", "Hoten": "Lê Kim Nam", "Ngaysinh": datetime(2003, 10, 20, tzinfo=timezone.utc), "Gioitinh": 0, "CCCD": "048203004295", "Quequan": "Đà Nẵng", "SDT": "0563499836", "Email": "lekimnam2809@gmail.com", "Lopsinhhoat": "21T1", "Nganhhoc": "Công nghệ thông tin", "Khoa": "Công nghệ số", "Nienkhoa": "2021-2025", "Dantoc": "Kinh", "Pass": "nam123"},
#     {"MSV": "21115053120111", "Hoten": "Hồ Bá Đông", "Ngaysinh": datetime(2003, 8, 18, tzinfo=timezone.utc), "Gioitinh": 0, "CCCD": "048203004296", "Quequan": "Đà Nẵng", "SDT": "0123456781", "Email": "hobadong2008@gmail.com", "Lopsinhhoat": "21T1", "Nganhhoc": "Công nghệ thông tin", "Khoa": "Công nghệ số", "Nienkhoa": "2021-2025", "Dantoc": "Kinh", "Pass": "dong123"},
#     {"MSV": "21115053120105", "Hoten": "Lê Hà Bình", "Ngaysinh": datetime(2003, 4, 24, tzinfo=timezone.utc), "Gioitinh": 0, "CCCD": "048203004297", "Quequan": "Đà Nẵng", "SDT": "0123456782", "Email": "lehabinh2404@gmail.com", "Lopsinhhoat": "21T1", "Nganhhoc": "Công nghệ thông tin", "Khoa": "Công nghệ số", "Nienkhoa": "2021-2025", "Dantoc": "Kinh", "Pass": "binh123"},
#     {"MSV": "21115053120138", "Hoten": "La Thế Quyền", "Ngaysinh": datetime(2003, 5, 15, tzinfo=timezone.utc), "Gioitinh": 0, "CCCD": "048203004298", "Quequan": "Đà Nẵng", "SDT": "0123456783", "Email": "lathequyen1505@gmail.com", "Lopsinhhoat": "21T1", "Nganhhoc": "Công nghệ thông tin", "Khoa": "Công nghệ số", "Nienkhoa": "2021-2025", "Dantoc": "Kinh", "Pass": "quyen123"},
#     {"MSV": "21115053120134", "Hoten": "Lê Thế Phú", "Ngaysinh": datetime(2003, 3, 14, tzinfo=timezone.utc), "Gioitinh": 0, "CCCD": "048203004299", "Quequan": "Đà Nẵng", "SDT": "0123456784", "Email": "lethephu2010@gmail.com", "Lopsinhhoat": "21T1", "Nganhhoc": "Công nghệ thông tin", "Khoa": "Công nghệ số", "Nienkhoa": "2021-2025", "Dantoc": "Kinh", "Pass": "phu123"},
#     {"MSV": "21115053120147", "Hoten": "Lê Hữu Thi", "Ngaysinh": datetime(2003, 4, 23, tzinfo=timezone.utc), "Gioitinh": 0, "CCCD": "048203004300", "Quequan": "Đà Nẵng", "SDT": "0123456785", "Email": "lehuuthi2703@gmail.com", "Lopsinhhoat": "21T1", "Nganhhoc": "Công nghệ thông tin", "Khoa": "Công nghệ số", "Nienkhoa": "2021-2025", "Dantoc": "Kinh", "Pass": "thi123"},
#     {"MSV": "21115053120158", "Hoten": "Lê Thanh Tuấn", "Ngaysinh": datetime(2003, 2, 12, tzinfo=timezone.utc), "Gioitinh": 0, "CCCD": "048203004301", "Quequan": "Đà Nẵng", "SDT": "0123456786", "Email": "lethanhtuan2902@gmail.com", "Lopsinhhoat": "21T1", "Nganhhoc": "Công nghệ thông tin", "Khoa": "Công nghệ số", "Nienkhoa": "2021-2025", "Dantoc": "Kinh", "Pass": "tuan123"},
#     {"MSV": "21115053120124", "Hoten": "Lê Quang Luân", "Ngaysinh": datetime(2003, 1, 11, tzinfo=timezone.utc), "Gioitinh": 0, "CCCD": "048203004302", "Quequan": "Đà Nẵng", "SDT": "0123456787", "Email": "lequangluan1501@gmail.com", "Lopsinhhoat": "21T1", "Nganhhoc": "Công nghệ thông tin", "Khoa": "Công nghệ số", "Nienkhoa": "2021-2025", "Dantoc": "Kinh", "Pass": "luan123"},
#     {"MSV": "21115053120150", "Hoten": "Đặng Văn Thống", "Ngaysinh": datetime(2003, 6, 21, tzinfo=timezone.utc), "Gioitinh": 0, "CCCD": "048203004303", "Quequan": "Đà Nẵng", "SDT": "0123456788", "Email": "dangvanthong1006@gmail.com", "Lopsinhhoat": "21T1", "Nganhhoc": "Công nghệ thông tin", "Khoa": "Công nghệ số", "Nienkhoa": "2021-2025", "Dantoc": "Kinh", "Pass": "thong123"},
#     {"MSV": "21115053120109", "Hoten": "Dương Ngọc Danh", "Ngaysinh": datetime(2003, 7, 21, tzinfo=timezone.utc), "Gioitinh": 0, "CCCD": "048203004304", "Quequan": "Đà Nẵng", "SDT": "0123456789", "Email": "duongngocdanh0711@gmail.com", "Lopsinhhoat": "21T1", "Nganhhoc": "Công nghệ thông tin", "Khoa": "Công nghệ số", "Nienkhoa": "2021-2025", "Dantoc": "Kinh", "Pass": "danh123"},
# ]

# for sv in sinh_vien_data:
#     sinh_vien = SinhVien(**sv)
#     sinh_vien.save()
    
# hinh_anh_data = [
#     {"TenHA": "ho-tro-giam-hoc-phi.png"},
#     {"TenHA": "quyet-dinh-giam-hoc-phi.png"},
#     {"TenHA": "mien-tru-hoc-phi.png"},
#     {"TenHA": "quyet-dinh-mien-tru-hoc-phi.png"},
#     {"TenHA": "mien-giam-va-ho-tro-hoc-phi.png"},
#     {"TenHA": "quyet-dinh-mien-giam-va-ho-tro-hoc-phi.png"},
#     {"TenHA": "ho-tro-chi-phi-hoc-tap.png"},
#     {"TenHA": "quyet-dinh-ho-tro-chi-phi-hoc-tap.png"},
#     {"TenHA": "Sổ-hộ-khẩu.png"},
#     {"TenHA": "Giấy-chứng-nhận-cư-trú.png"},
#     {"TenHA": "Chứng-minh-khó-khăn.png"},
#     {"TenHA": "Thư-giới-thiệu-phường-xã.png"},
# ]

# for ha in hinh_anh_data:
#     hinh_anh = HinhAnh(**ha)
#     hinh_anh.save()
     
# dai_dien_data = [
#     {"MNV" : "1234567890", "Hoten": "Võ Trung Hùng", "Ngaysinh": datetime(1980, 10, 20, tzinfo=timezone.utc), "Gioitinh": 0, "SDT": "01234567890", "Email": "votrunghung@gmail.com", "Roles": 1, "Pass": "hung123"},
#     {"MNV" : "1234567891", "Hoten": "Nguyễn Thị Hà Quyên", "Ngaysinh": datetime(1980, 2, 10, tzinfo=timezone.utc), "Gioitinh": 1, "SDT": "01234567891", "Email": "nguyenthihaquyen@gmail.com", "Roles": 2, "Pass": "quyen123"},
# ]

# for dd in dai_dien_data:
#     dai_dien = DaiDienPhongBan(**dd)
#     dai_dien.save()
    
# bai_viet_data = [
#     {"Noidung": "Thông báo: Chính sách hỗ trợ giảm 5% học phí học kỳ I năm học 2023-2024 đối với sinh viên có hoàn cảnh khó khăn. Thông tin chi tiết, xem tại: daotao.ute.udn.vn.", "Ngaydang": datetime(2024, 4, 10, 7, 0, 0, tzinfo=timezone.utc), "NgayhetHieuluc": datetime(2024, 4, 24, 7, 0, 0, tzinfo=timezone.utc), "MNV": "1234567890"},
#     {"Noidung": "Thông báo: Nghị định 81/2021/NĐ-CP ngày 27/8/2021 quy định 2 đối tượng không phải đóng học phí gồm: Học sinh tiểu học trường công lập; Người theo học các ngành chuyên môn đặc thù đáp ứng yêu cầu phát triển kinh tế - xã hội, quốc phòng, an ninh theo quy định của Luật Giáo dục đại học, các ngành chuyên môn đặc thù do Thủ tướng Chính phủ quy định. Xem thêm tại: http://sotaysinhvien.ute.udn.vn/ChuyenMucs/Mien-giam-hoc-phi_37.html", "Ngaydang": datetime(2024, 4, 10, 7, 0, 0, tzinfo=timezone.utc), "NgayhetHieuluc": datetime(2024, 4, 24, 7, 0, 0, tzinfo=timezone.utc), "MNV": "1234567890"},
#     {"Noidung": "Thông báo: Nghị định của Chính phủ quy định các nhóm đối tượng được giảm học phí và hỗ trợ tiền đóng học phí. Xem thêm tại: http://sotaysinhvien.ute.udn.vn/ChuyenMucs/Mien-giam-hoc-phi_37.html", "Ngaydang": datetime(2024, 4, 10, 7, 0, 0, tzinfo=timezone.utc), "NgayhetHieuluc": datetime(2024, 4, 24, 7, 0, 0, tzinfo=timezone.utc), "MNV": "1234567890"},
#     {"Noidung": "Thông báo: Đối tượng được hỗ trợ chi phí học tập: - Sinh viên là người dân tộc thiểu số thuộc hộ nghèo và hộ cận nghèo theo quy định của Thủ tướng chính phủ phê duyệt theo từng thời kỳ; - Không áp dụng đối với sinh viên: Cử tuyển, các đối tượng chính sách được xét tuyển, đào tạo theo địa chỉ, đào tạo liên thông, vừa làm vừa học, văn bằng 2 và học đại học, cao đẳng sau khi hoàn thành chương trình dự bị đại học. Xem thêm tại: http://sotaysinhvien.ute.udn.vn/ChuyenMucs/Mien-giam-hoc-phi_37.html", "Ngaydang": datetime(2024, 4, 10, 7, 0, 0, tzinfo=timezone.utc), "NgayhetHieuluc": datetime(2024, 4, 24, 7, 0, 0, tzinfo=timezone.utc), "MNV": "1234567890"},
# ]

# bai_viet_objects = []
# for bv in bai_viet_data:
#     bv['MNV'] = DaiDienPhongBan.objects.get(pk=bv['MNV'])  # Ensure correct foreign key assignment
#     bai_viet = BaiViet(**bv)
#     bai_viet_objects.append(bai_viet)

# BaiViet.objects.bulk_create(bai_viet_objects)
    
# quy_dinh_data = [
#     {"MBV": 1, "MDT": 23, "MTC": 7},
#     {"MBV": 4, "MDT": 23, "MTC": 7},
#     {"MBV": 4, "MDT": 23, "MTC": 8},
#     {"MBV": 4, "MDT": 23, "MTC": 15},
#     {"MBV": 4, "MDT": 23, "MTC": 16},
# ]

# quy_dinh_objects = []
# for qd in quy_dinh_data:
#     try:
#         qd['MBV'] = BaiViet.objects.get(pk=qd['MBV'])  # Đảm bảo khóa ngoại chính xác
#         qd['MDT'] = DoiTuongChinhSach.objects.get(pk=qd['MDT'])
#         qd['MTC'] = TieuChi.objects.get(pk=qd['MTC'])
        
#         # Kiểm tra xem QuyDinhApDung đã tồn tại hay chưa
#         if not QuyDinhApDung.objects.filter(MBV=qd['MBV'], MDT=qd['MDT'], MTC=qd['MTC']).exists():
#             quy_dinh = QuyDinhApDung(**qd)
#             quy_dinh_objects.append(quy_dinh)
#         else:
#             print(f"QuyDinhApDung with MBV: {qd['MBV'].pk}, MDT: {qd['MDT'].pk}, MTC: {qd['MTC'].pk} already exists.")
#     except (BaiViet.DoesNotExist, DoiTuongChinhSach.DoesNotExist, TieuChi.DoesNotExist) as e:
#         print(f"Error: {e}")

# # Tạo các đối tượng QuyDinhApDung trong cơ sở dữ liệu nếu có đối tượng mới
# if quy_dinh_objects:
#     QuyDinhApDung.objects.bulk_create(quy_dinh_objects)
# else:
#     print("No new QuyDinhApDung objects to create.")

    
# hinh_anh_bai_viet_data = [
#     {"MHA": 1, "MBV": 1},
#     {"MHA": 2, "MBV": 1},
#     {"MHA": 3, "MBV": 2},
#     {"MHA": 4, "MBV": 2},
#     {"MHA": 5, "MBV": 3},
#     {"MHA": 6, "MBV": 3},
#     {"MHA": 7, "MBV": 4},
#     {"MHA": 8, "MBV": 4},
# ]

# hinh_anh_bai_viet_objects = []
# for habv in hinh_anh_bai_viet_data:
#     habv['MHA'] = HinhAnh.objects.get(pk=habv['MHA'])  # Ensure correct foreign key assignment
#     habv['MBV'] = BaiViet.objects.get(pk=habv['MBV'])
#     hinh_anh_bai_viet = HinhAnhBaiViet(**habv)
#     hinh_anh_bai_viet_objects.append(hinh_anh_bai_viet)

# HinhAnhBaiViet.objects.bulk_create(hinh_anh_bai_viet_objects)
    
# ho_so_data = [
#     # {"MSV": "21115053120128", "MNV": "1234567891", "MotaHoancanhKhokhan": "", "TrangthaiXacnhan": 0, "Ngaydangky": datetime(2024, 4, 11, 7, 0, 0, tzinfo=timezone.utc), "TrangthaiXetduyet": 0, "Ngayxetduyet": datetime(2024, 4, 30, 7, 0, 0, tzinfo=timezone.utc), "Hocki": "223", "MDT": 20},
#     # {"MSV": "21115053120111", "MNV": "1234567891", "MotaHoancanhKhokhan": "", "TrangthaiXacnhan": 1, "Ngaydangky": datetime(2024, 4, 11, 7, 0, 0, tzinfo=timezone.utc), "TrangthaiXetduyet": 1, "Ngayxetduyet": datetime(2024, 4, 30, 7, 0, 0, tzinfo=timezone.utc), "Hocki": "223", "MDT": 20},
#     # {"MSV": "21115053120105", "MNV": "1234567891", "MotaHoancanhKhokhan": "", "TrangthaiXacnhan": 0, "Ngaydangky": datetime(2024, 4, 11, 7, 0, 0, tzinfo=timezone.utc), "TrangthaiXetduyet": 0, "Ngayxetduyet": datetime(2024, 6, 1, 7, 0, 0, tzinfo=timezone.utc), "Hocki": "223", "MDT": 20},
#     {"MSV": "21115053120109", "MNV": "1234567891", "MotaHoancanhKhokhan": "", "TrangthaiXacnhan": 0, "Ngaydangky": datetime(2024, 4, 10, 7, 0, 0, tzinfo=timezone.utc), "Ngayxacnhan": datetime(2024, 4, 10, 7, 0, 0, tzinfo=timezone.utc),"TrangthaiXetduyet": 0, "Ngayxetduyet": datetime(2024, 6, 1, 7, 0, 0, tzinfo=timezone.utc), "Hocki": "223", "MDT": 20},
# ]

# ho_so_objects = []
# for hs in ho_so_data:
#     hs['MSV'] = SinhVien.objects.get(pk=hs['MSV'])  # Ensure correct foreign key assignment
#     hs['MNV'] = DaiDienPhongBan.objects.get(pk=hs['MNV'])
#     hs['MDT'] = DoiTuongChinhSach.objects.get(pk=hs['MDT'])
#     ho_so = HoSoDangKy(**hs)
#     ho_so_objects.append(ho_so)

# HoSoDangKy.objects.bulk_create(ho_so_objects)

# chi_tiet_ho_so_data = [
#     {"MHSDK": 3, "MTC": 8, "MHA": 9},
#     {"MHSDK": 3, "MTC": 15, "MHA": 10},
#     {"MHSDK": 3, "MTC": 16, "MHA": 11},
#     {"MHSDK": 3, "MTC": 17, "MHA": 12},
# ]

# chi_tiet_ho_so_objects = []
# for cths in chi_tiet_ho_so_data:
#     cths['MHSDK'] = HoSoDangKy.objects.get(pk=cths['MHSDK'])
#     cths['MTC'] = TieuChi.objects.get(pk=cths['MTC'])
#     cths['MHA'] = HinhAnh.objects.get(pk=cths['MHA'])
#     chi_tiet_ho_so = ChiTietHoSo(**cths)
#     chi_tiet_ho_so_objects.append(chi_tiet_ho_so)
    
# ChiTietHoSo.objects.bulk_create(chi_tiet_ho_so_objects)







