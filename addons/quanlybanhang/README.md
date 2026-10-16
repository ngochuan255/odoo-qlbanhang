# QLBanHang - Quanlybanhang

Module thực hành dựa trên `odoo-Bai thuc hanh.pdf`, dành cho Odoo 20.0 trong dự án này. Tên thư mục/tên kỹ thuật là `quanlybanhang`; tên hiển thị là **QLBanHang**, tác giả **Than Ngoc Huan**.

## Chức năng

Ứng dụng **Quản lý Bán Hàng** gồm:

| Menu | Model | Trường dữ liệu |
| --- | --- | --- |
| Quản lý hãng | `hang` | `tenhang`, `mahang`, `diachi`, `sodt` |
| Quản lý nhân viên | `quanlybanhang.nhanvien` | `tennv`, `manv`, `gioitinh`, `sdt` |
| Quản lý sản phẩm | `sanpham` | `masp`, `tensp`, `soluong`, `giaban`, `mausac` |

Các model có danh sách, biểu mẫu, action và menu. Kiểu dữ liệu, nhãn và các trường bắt buộc theo phần mô tả trong PDF. Tên hãng, nhân viên và sản phẩm được dùng làm tên hiển thị của bản ghi.

Người dùng nội bộ có quyền tạo, đọc, sửa, xóa. Tài khoản portal và khách không được cấp quyền. Nhập dữ liệu và xuất dữ liệu dùng chức năng chuẩn của Odoo; xuất dữ liệu yêu cầu quyền **Export Data** của Odoo.

## Những điểm điều chỉnh theo môi trường hiện tại

- Odoo 20 dùng `<list>`/`list,form` và quyền `ir.access.csv` với thao tác `crud`, thay cú pháp Odoo cũ.
- PDF dùng `_name = 'nhanvien'`, nhưng model này đang thuộc module `ql_nhansu`. Bài bán hàng dùng `quanlybanhang.nhanvien` để có dữ liệu, trường và biểu mẫu riêng; không phụ thuộc hoặc sửa module nhân sự.
- Phần mô tả sản phẩm quy định ba màu **Xanh/Đỏ/Vàng**, trong khi hình VF3 ghi **Xám**. Module giữ đúng ba lựa chọn được mô tả và dùng **Vàng** cho bản ghi mẫu VF3.
- Hình danh sách sản phẩm ghi cột “Mã Hãng”, trong khi phần mô tả yêu cầu trường `masp` là **Mã sản phẩm**, kiểu Char. Module dùng nhãn **Mã sản phẩm**, với các mã mẫu 3/2/1 và giữ được số 0 đầu khi nhập mã.
- Giữ tên mẫu **Nikia i10** và các số điện thoại như hình, kể cả số có 11 chữ số.

## Dữ liệu mẫu

| Hãng | Mã hãng | Địa chỉ | Số điện thoại |
| --- | --- | --- | --- |
| Samsung | 1 | Hàn Quốc | 09282828282 |
| Nokia | 2 | Phần Lan | 0928272722 |
| Vinfast | 3 | Việt Nam | 0928272727 |

| Nhân viên | Mã nhân viên | Giới tính | Điện thoại |
| --- | --- | --- | --- |
| Lê Việt Anh | 1 | Nam | 09865544333 |
| Phan Tuấn Quỳnh | 2 | Nam | 0927272772 |
| Trần Minh Tuấn | 3 | Nam | 02927272727 |
| Vũ Hoàng Vân | 4 | Nữ | 0872727272 |

| Sản phẩm | Mã sản phẩm | Số lượng | Giá bán | Màu sắc |
| --- | --- | --- | --- | --- |
| VF3 | 3 | 100 | 270000 | Vàng |
| Nikia i10 | 2 | 20 | 50000 | Đỏ |
| Galaxy X25 | 1 | 200 | 2500000 | Xanh |

Dữ liệu nằm trong `demo/quanlybanhang_demo.xml`, có XML ID và `noupdate="1"` để giữ chỉnh sửa khi nâng cấp. Odoo chỉ tự nạp file này khi cơ sở dữ liệu bật chế độ demo. Cơ sở dữ liệu `huan_db` hiện tại đã bật demo.

## Sử dụng

Mở `http://localhost:8071/odoo?db=huan_db`, đăng nhập và chọn **Quản lý Bán Hàng**. Để xem thông tin ứng dụng, vào **Apps/Ứng dụng**, tìm `quanlybanhang`, mở menu ba chấm và chọn **Module Info/Thông tin mô-đun**.

Module chỉ phụ thuộc `base`. Nếu cài trên máy khác, chép thư mục `quanlybanhang` vào đường dẫn addons, khởi động lại Odoo, cập nhật danh sách ứng dụng rồi cài **QLBanHang**.

Nâng cấp mã nguồn từ PowerShell tại thư mục dự án:

```powershell
docker compose stop web
try {
    docker compose run --rm --no-deps -T web odoo -c /etc/odoo/odoo.conf -d huan_db -u quanlybanhang --stop-after-init --no-http
} finally {
    docker compose start web
}
```

Nếu cài lần đầu, thay `-u` bằng `-i`. Không dùng phiên bản này nguyên trạng trên Odoo cũ vì cấu hình quyền của Odoo 20 đã thay đổi.

## Kiểm tra

`tests/test_quanlybanhang.py` kiểm tra CRUD qua cả ba biểu mẫu, chặn đọc dữ liệu bằng tài khoản portal và nhập/xuất sản phẩm có mã bắt đầu bằng số 0.

Chạy trên cơ sở dữ liệu kiểm thử riêng:

```powershell
docker compose exec -T web odoo -c /etc/odoo/odoo.conf -d quanlybanhang_verify_20261016 -i quanlybanhang,ql_nhansu --test-tags /quanlybanhang,/ql_nhansu --http-port=8079 --workers=0 --max-cron-threads=0
```

Ở những lần chạy tiếp theo, thay `-i` bằng `-u`. Các thao tác kiểm thử được hoàn tác sau mỗi bài kiểm tra.
