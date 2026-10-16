# -*- coding: utf-8 -*-
from odoo import fields, models


class Hang(models.Model):
    _name = 'hang'
    _description = 'Hãng'
    _rec_name = 'tenhang'

    tenhang = fields.Char(string='Tên hãng', required=True)
    mahang = fields.Integer(string='Mã hãng', required=True)
    diachi = fields.Char(string='Địa chỉ', required=True)
    sodt = fields.Char(string='Số điện thoại', required=True)


class NhanVien(models.Model):
    # Tách model để cùng cài được với model nhanvien của ql_nhansu.
    _name = 'quanlybanhang.nhanvien'
    _description = 'Nhân viên bán hàng'
    _rec_name = 'tennv'

    tennv = fields.Char(string='Họ và tên', required=True)
    manv = fields.Integer(string='Mã nhân viên', required=True)
    gioitinh = fields.Selection(
        [('nam', 'Nam'), ('nu', 'Nữ')],
        string='Giới tính',
    )
    sdt = fields.Char(string='Điện thoại')


class SanPham(models.Model):
    _name = 'sanpham'
    _description = 'Sản phẩm'
    _rec_name = 'tensp'

    masp = fields.Char(string='Mã sản phẩm', required=True)
    tensp = fields.Char(string='Tên sản phẩm', required=True)
    soluong = fields.Integer(string='Số lượng', required=True)
    giaban = fields.Integer(string='Giá bán', required=True)
    mausac = fields.Selection(
        [('xanh', 'Xanh'), ('do', 'Đỏ'), ('vang', 'Vàng')],
        string='Màu sắc',
    )
