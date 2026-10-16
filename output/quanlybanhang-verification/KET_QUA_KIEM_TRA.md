# Kết quả kiểm tra Quanlybanhang

Ngày kiểm tra: 16/10/2026. Môi trường: Odoo Server 20.0-20261015, PostgreSQL 16, Docker Compose của dự án.

## Kết quả

- Module kỹ thuật `quanlybanhang`, tên hiển thị **QLBanHang**, tác giả **Than Ngoc Huan**, phiên bản `20.0.1.0.0` đã được cài vào `huan_db`.
- Menu **Quản lý Bán Hàng** có **Quản lý hãng**, **Quản lý nhân viên**, **Quản lý sản phẩm**.
- Đã nạp 3 hãng, 4 nhân viên bán hàng và 3 sản phẩm mẫu theo hình trong PDF, với các điều chỉnh được nêu dưới đây.
- Logo được trích từ hình minh họa trong PDF.
- Kiểm tra cú pháp Python, XML và đường dẫn tài nguyên trong manifest: đạt.

## Kiểm tra tích hợp

Đã chạy cùng lúc bộ kiểm tra của hai module trên cơ sở dữ liệu kiểm thử riêng:

| Nội dung | Kết quả |
| --- | --- |
| CRUD hãng qua biểu mẫu với người dùng nội bộ | Đạt |
| CRUD nhân viên bán hàng qua biểu mẫu với người dùng nội bộ | Đạt |
| CRUD sản phẩm qua biểu mẫu với người dùng nội bộ | Đạt |
| Chặn tài khoản portal đọc cả ba model | Đạt |
| Nhập/xuất sản phẩm, giữ mã 0007 và các giá trị số | Đạt |
| Ba bài kiểm tra hiện có của ql_nhansu | Đạt |

Log Odoo: **0 failed, 0 errors, 8 test methods**; gồm 5 bài của `quanlybanhang` và 3 bài của `ql_nhansu`. Xem `integration-tests.log`. Các trường hợp con được Odoo thống kê riêng.

Ngoài ra, đã so sánh dấu kiểm dữ liệu phòng và nhân viên của `ql_nhansu` trước/sau khi cài module bán hàng; dữ liệu giữ nguyên.

## Kiểm tra trình duyệt

Đã dùng Chromium headless mở ứng dụng thật tại `http://localhost:8071` trên `huan_db`, kiểm tra:

- Ba danh sách hiển thị đủ bản ghi và số điện thoại giữ số 0 đầu.
- Ba biểu mẫu có đủ trường theo yêu cầu.
- Danh sách chọn màu có Xanh, Đỏ, Vàng.
- Trang Module Info hiển thị QLBanHang, By Than Ngoc Huan, tóm tắt, danh mục và logo.
- Không ghi nhận lỗi JavaScript chưa được xử lý trong lượt kiểm tra cuối.

Ảnh xác minh: `hang.png`, `nhanvien.png`, `sanpham.png`, các ảnh `*-form.png` và `module-info.png`.

## Điều chỉnh có chủ đích

- Dùng cú pháp danh sách và phân quyền phù hợp Odoo 20.
- Model nhân viên bán hàng là `quanlybanhang.nhanvien` để tránh trùng `nhanvien` của module nhân sự; các trường của bài bán hàng giữ theo PDF.
- Phần mô tả trong PDF quy định ba màu Xanh/Đỏ/Vàng, nhưng hình VF3 ghi Xám. Module theo phần mô tả và dùng Vàng cho VF3.
- Dùng trường `masp` và nhãn Mã sản phẩm theo phần yêu cầu, thay nhãn Mã Hãng xuất hiện trong hình sản phẩm.

## Trạng thái bàn giao

Đã xóa tài khoản, mật khẩu tạm và cơ sở dữ liệu kiểm thử. Hai ứng dụng vẫn cài trong `huan_db`; dịch vụ Odoo và PostgreSQL tiếp tục chạy.

Phạm vi xác minh là phiên bản Odoo 20 đang chạy trong dự án này.
