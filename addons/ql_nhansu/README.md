# Quản lý nhân sự - ql_nhansu

Module thực hành theo file `Xay dung module odoo.pdf`, điều chỉnh cú pháp để chạy trên Odoo 20.0 trong dự án này.

## Thông tin ở Bước 6

- Tên ứng dụng: **Than Ngoc Huan - 2023606980**.
- Tác giả: **Than Ngoc Huan**. Odoo hiển thị dòng **By Than Ngoc Huan** khi dùng giao diện tiếng Anh.
- Tóm tắt: Thực hành lập trình Odoo.
- Mô tả: Học lập trình Odoo - Hệ quản trị doanh nghiệp điện tử ERP.
- Loại: Hệ thống thông tin; giấy phép LGPL-3.
- Logo lấy từ hình minh họa trong tài liệu.

## Các chức năng theo mẫu

Menu **Quản lý nhân sự** có hai mục:

| Menu | Model | Trường dữ liệu |
| --- | --- | --- |
| Quản lý phòng | `phong` | Tên phòng (`name`, bắt buộc), mã phòng (`depid`, số nguyên, bắt buộc) |
| Quản lý nhân viên | `nhanvien` | Họ và tên (`name`, bắt buộc), mã nhân viên (`empid`, số nguyên, bắt buộc), giới tính (`gender`: Nam/Nữ), điện thoại (`phone`) |

Người dùng nội bộ có quyền thêm, xem, sửa, xóa. Tài khoản portal và khách không được cấp quyền truy cập các model này.

## Dữ liệu mẫu ở Bước 10

| Phòng | Mã phòng |
| --- | --- |
| Nhân sự | 100 |
| Kế hoạch | 120 |

| Nhân viên | Mã nhân viên | Giới tính | Điện thoại |
| --- | --- | --- | --- |
| Than Ngoc Huan | 2023606980 | Chưa cung cấp | Chưa cung cấp |
| Nguyễn Thị Hoa | 11111 | Nữ | 0901111111 |
| Bùi Văn Bình | 22222 | Nam | 0902222222 |

Giới tính và điện thoại của Than Ngoc Huan được để trống để điền thông tin thật. Các bản ghi mẫu có XML ID và `noupdate="1"`, giúp giữ lại chỉnh sửa của người dùng khi nâng cấp module.

Dữ liệu mẫu nằm trong `demo/demo.xml` và được Odoo nạp khi cơ sở dữ liệu bật chế độ demo. Cơ sở dữ liệu `huan_db` hiện tại đã có các bản ghi trên.

## Mở module trong dự án hiện tại

1. Mở `http://localhost:8071/odoo?db=huan_db` và đăng nhập tài khoản Odoo của bạn.
2. Chọn ứng dụng **Quản lý nhân sự**, rồi chọn **Quản lý phòng** hoặc **Quản lý nhân viên**.
3. Trong **Ứng dụng**, tìm theo tên kỹ thuật `ql_nhansu` hoặc tên **Than Ngoc Huan - 2023606980** để xem thông tin Bước 6.

Module đã được cài vào `huan_db`. Nếu sửa mã Python hoặc XML sau này, nâng cấp từ PowerShell tại thư mục dự án:

```powershell
docker compose stop web
try {
    docker compose run --rm --no-deps -T web odoo -c /etc/odoo/odoo.conf -d huan_db -u ql_nhansu --stop-after-init --no-http
} finally {
    docker compose start web
}
```

Nếu cài vào một cơ sở dữ liệu khác, dùng `-i ql_nhansu` thay cho `-u ql_nhansu`, và thay tên cơ sở dữ liệu tương ứng.

## Những thay đổi cần thiết cho Odoo 20

- Giữ tên kỹ thuật `ql_nhansu` theo yêu cầu, thay tên `kiemtra2` trong tài liệu.
- Dùng `<list>` và `list,form` thay cho `<tree>` và `tree,form`.
- Dùng `security/ir.access.csv`, model quyền `ir.access` và thao tác `crud` thay định dạng `ir.model.access.csv` của Odoo cũ.
- Phiên bản module là `20.0.1.0.0` để phù hợp Odoo đang chạy.

## Kiểm tra tích hợp

Các bài kiểm tra ở `tests/test_ql_nhansu.py` chạy biểu mẫu thật với tài khoản nội bộ và kiểm tra việc chặn tài khoản portal.

Chạy trên cơ sở dữ liệu kiểm thử riêng, không dùng `huan_db`:

```powershell
docker compose exec -T web odoo -c /etc/odoo/odoo.conf -d ql_nhansu_verify_20261016 -i ql_nhansu --test-tags /ql_nhansu --http-port=8079 --workers=0 --max-cron-threads=0
```

Ở những lần chạy tiếp theo, dùng `-u` thay cho `-i`. Các kiểm tra sử dụng transaction và tự hoàn tác dữ liệu kiểm thử. Cơ sở dữ liệu kiểm thử riêng đã được dọn sau lần xác minh bàn giao.
