# Kết quả kiểm tra ql_nhansu

Ngày kiểm tra: 16/10/2026. Môi trường: Docker Compose của dự án, Odoo Server 20.0-20261015, PostgreSQL 16.

## Kết quả

- Module `ql_nhansu` đã cài trong cơ sở dữ liệu `huan_db`, phiên bản `20.0.1.0.0`.
- Trang thông tin ứng dụng hiển thị **Than Ngoc Huan - 2023606980**, **By Than Ngoc Huan**, logo, danh mục, giấy phép, tóm tắt và mô tả.
- Menu **Quản lý nhân sự** mở được **Quản lý phòng** và **Quản lý nhân viên**.
- Dữ liệu mẫu gồm 2 phòng và 3 nhân viên; mã sinh viên `2023606980` hiển thị đầy đủ.
- Giới tính và điện thoại của Than Ngoc Huan để trống do chưa có thông tin.
- Kiểm tra cú pháp Python, XML và đường dẫn trong manifest: đạt.

## Kiểm tra tích hợp tự động

Các bài kiểm tra dùng Odoo `Form`, tài khoản nội bộ thật và quyền truy cập thực tế trên cơ sở dữ liệu kiểm thử riêng:

1. Tạo, đọc, sửa, xóa phòng qua biểu mẫu: đạt.
2. Tạo, đọc, sửa, xóa nhân viên qua biểu mẫu: đạt.
3. Tài khoản portal bị chặn đọc cả hai model: đạt.

Kết quả Odoo: **0 failed, 0 errors, 3 test methods**. Hai trường hợp con về quyền truy cập được tính riêng trong thống kê chi tiết của Odoo. Log ở `ql_nhansu-tests.log`.

## Kiểm tra giao diện

Đã mở ứng dụng thật tại `http://localhost:8071` bằng Chromium headless và tài khoản kiểm thử tạm trong `huan_db`:

- Danh sách nhân viên: đạt; kiểm tra họ tên, mã sinh viên đầy đủ và dấu tiếng Việt.
- Danh sách phòng: đạt; kiểm tra hai phòng Nhân sự và Kế hoạch.
- Trang Module Info: đạt; kiểm tra tên ứng dụng, tác giả, tóm tắt và quan sát logo.
- Không ghi nhận lỗi JavaScript chưa được xử lý trong lượt kiểm tra cuối.

Ảnh giao diện: `module-info.png`, `phong.png`, `nhanvien.png`.

## Trạng thái sau kiểm tra

Đã xóa tài khoản kiểm thử, mật khẩu tạm và cơ sở dữ liệu kiểm thử. Odoo và PostgreSQL vẫn chạy; `huan_db` còn đủ dữ liệu mẫu.

Phạm vi tương thích đã kiểm tra là Odoo 20 của dự án. Bản này dùng `<list>`, định dạng quyền `ir.access.csv` và phiên bản tương ứng; không dùng nguyên cú pháp Odoo cũ trong PDF.
