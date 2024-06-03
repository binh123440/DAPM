Tesseract là thư viện OCR(Optical Character Recognition), Chuyên dùng để đọc các ký tự trong ảnh rồi chuyển thành text để giảm công sức đánh máy. Trong đó phổ biến nhất là nhận diện văn bản bằng Tesseract. nổi tiếng do độ chính xác cao hơn hẳn các thư viên khác. Tesseract có thể chạy độc lập hoặc tích hợp với OpenCV đều được. Nếu chạy độc lập thì Tesseract sử dụng thư viện leptonica để đọc hình ảnh.
Trong code của tôi có sửa dụng tesseract để chuyển từ ảnh sang text:

****![image](https://github.com/binh123440/DAPM/assets/144503606/79dd7a82-a631-4efe-834c-d68e1a9b0f75)

Hãy tải và cài đặt Tesseract ở đường link sau: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.4.20240503.exe

Hoặc bạn có thể tải ở Trang chủ của Tesseract : https://github.com/UB-Mannheim/tesseract/wiki

![image](https://github.com/binh123440/DAPM/assets/144503606/583c69f3-e656-4dcf-bc14-276a45bcecad)

và điều chỉnh trong file view thành đường dẫn tới file tesseract.exe mà bạn đã cài

Đây là phiên bản mà tôi đã cài và sử dụng trong dự án trên:

![image](https://github.com/binh123440/DAPM/assets/144503606/5da72911-0f99-4abf-bf13-7fbaa087e078)

Đồng thời chạy dòng lệnh này để có add thê thư viện Tesseract vào dự án:

pip install pytesseract
