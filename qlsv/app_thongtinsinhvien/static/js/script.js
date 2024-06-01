document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const messageContainer = document.getElementById("message-container");
    const overlay = document.getElementById("overlay");

    form.addEventListener('submit', function (event) {
        event.preventDefault();

        fetch(form.action, {
            method: 'POST',
            body: new FormData(form)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                messageContainer.textContent = data.message;
                messageContainer.style.display = "block";
                overlay.style.display = "block";
            } else {
                messageContainer.textContent = "Ngày sinh không hợp lệ. Vui lòng nhập theo định dạng YYYY-MM-DD."; // Hoặc thông báo lỗi cụ thể từ server
                messageContainer.style.display = "block";
                overlay.style.display = "block";
            }

            setTimeout(() => {
                messageContainer.style.display = "none";
                overlay.style.display = "none";
            }, 3000);
        })
        .catch(error => {
            console.error('Lỗi khi gửi yêu cầu:', error);
        });
    });
});
