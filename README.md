# Odoo Thực Hành

Dự án thực hành Odoo của **Than Ngoc Huan - 2023606980**, gồm hai module theo tài liệu PDF trong repository.

| Module kỹ thuật | Tên hiển thị | Chức năng |
| --- | --- | --- |
| `ql_nhansu` | Than Ngoc Huan - 2023606980 | Quản lý phòng và nhân viên |
| `quanlybanhang` | QLBanHang | Quản lý hãng, nhân viên bán hàng và sản phẩm |

Cả hai module dùng tác giả **Than Ngoc Huan**, giấy phép LGPL-3 và chạy trên **Odoo 20.0**. Dự án sử dụng PostgreSQL 16 và Docker Compose.

## Cấu trúc

```text
addons/
  ql_nhansu/                 # Module quản lý nhân sự, dữ liệu mẫu và kiểm tra
  quanlybanhang/             # Module quản lý bán hàng, dữ liệu mẫu và kiểm tra
config/
  odoo.conf.example          # Cấu hình mẫu; sao chép thành odoo.conf trước khi chạy
compose.yaml                # Odoo 20 và PostgreSQL 16, cổng Odoo 8071
output/
  ql_nhansu.zip
  quanlybanhang.zip
  verification/             # Kết quả và ảnh của module nhân sự
  quanlybanhang-verification/# Kết quả và ảnh của module bán hàng
Xay dung module odoo.pdf
odoo-Bai thuc hanh.pdf
```

## Khởi động sau khi clone

Yêu cầu Docker Desktop có hỗ trợ Docker Compose và Linux containers. Chạy từ PowerShell tại thư mục dự án:

```powershell
Copy-Item -LiteralPath 'config/odoo.conf.example' -Destination 'config/odoo.conf'
```

Mở `config/odoo.conf`, đổi `admin_passwd` thành mật khẩu quản trị cơ sở dữ liệu của bạn, rồi chạy:

```powershell
docker compose up -d
```

1. Truy cập [Odoo trên localhost:8071](http://localhost:8071).
2. Tạo cơ sở dữ liệu, ví dụ `huan_db`, và tài khoản quản trị Odoo. Bật dữ liệu demo nếu muốn nạp các bản ghi mẫu theo bài thực hành.
3. Bật chế độ nhà phát triển, vào **Apps/Ứng dụng → Update Apps List/Cập nhật danh sách ứng dụng**.
4. Tìm và cài `ql_nhansu` cùng `quanlybanhang`.
5. Mở **Quản lý nhân sự** hoặc **Quản lý Bán Hàng** từ danh sách ứng dụng.

Cấu hình `odoo.conf` đang sử dụng trên máy và các volume cơ sở dữ liệu không được lưu vào Git. PostgreSQL dùng tài khoản `odoo`/`odoo` cho môi trường thực hành; chỉ dịch vụ Odoo được ánh xạ ra cổng máy chủ trong Compose.

## Chi tiết các module

- [Hướng dẫn ql_nhansu](addons/ql_nhansu/README.md)
- [Hướng dẫn quanlybanhang](addons/quanlybanhang/README.md)

`quanlybanhang` dùng model nhân viên riêng `quanlybanhang.nhanvien` để chạy cùng model `nhanvien` của `ql_nhansu`. Màu sản phẩm gồm Xanh/Đỏ/Vàng theo phần yêu cầu trong PDF; bản ghi VF3 dùng Vàng. Những khác biệt giữa phần mô tả và hình minh họa được ghi rõ trong README của module.

## Kiểm tra và kết quả đã lưu

Đã chạy 8 bài kiểm tra tích hợp của hai module trên Odoo 20, gồm CRUD qua biểu mẫu, quyền truy cập và nhập/xuất dữ liệu. Log kết quả: **0 failures, 0 errors**. Ba danh sách và ba biểu mẫu bán hàng cùng trang thông tin module đã được kiểm tra bằng Chromium trên ứng dụng chạy thật.

- [Báo cáo nhân sự](output/verification/KET_QUA_KIEM_TRA.md)
- [Báo cáo bán hàng](output/quanlybanhang-verification/KET_QUA_KIEM_TRA.md)
- [Log kiểm tra hai module](output/quanlybanhang-verification/integration-tests.log)
- [Giao diện QLBanHang](output/quanlybanhang-verification/module-info.png)

Để chạy lại kiểm tra, dùng hướng dẫn trong README của module với cơ sở dữ liệu kiểm thử riêng. Ảnh và log là bằng chứng của lần kiểm tra bàn giao ngày 16/10/2026; dữ liệu của từng lần khởi động mới phụ thuộc cơ sở dữ liệu và lựa chọn nạp demo.
