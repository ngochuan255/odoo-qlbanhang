from odoo.exceptions import AccessError
from odoo.tests import Form, TransactionCase, tagged
from odoo.tests.common import new_test_user


@tagged('post_install', '-at_install')
class TestQuanLyBanHang(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.internal_user = new_test_user(
            cls.env,
            login='quanlybanhang_internal',
            groups='base.group_user,base.group_allow_export',
        )
        cls.portal_user = new_test_user(
            cls.env, login='quanlybanhang_portal', groups='base.group_portal'
        )

    def test_internal_user_manages_brands_from_form(self):
        self.assertIn('hang', self.env.registry)
        with Form(self.env['hang'].with_user(self.internal_user)) as form:
            form.tenhang = 'Samsung'
            form.mahang = 1
            form.diachi = 'Hàn Quốc'
            form.sodt = '09282828282'
        brand = form.record
        self.assertEqual(brand.display_name, 'Samsung')
        self.assertEqual(brand.sodt, '09282828282')
        with Form(brand) as form:
            form.diachi = 'Việt Nam'
        self.assertEqual(brand.diachi, 'Việt Nam')
        brand.unlink()
        self.assertFalse(brand.exists())

    def test_internal_user_manages_products_from_form(self):
        self.assertIn('sanpham', self.env.registry)
        with Form(self.env['sanpham'].with_user(self.internal_user)) as form:
            form.masp = '001'
            form.tensp = 'Galaxy X25'
            form.soluong = 200
            form.giaban = 2500000
            form.mausac = 'xanh'
        product = form.record
        self.assertEqual(product.display_name, 'Galaxy X25')
        self.assertEqual(product.masp, '001')
        self.assertEqual(product.giaban, 2500000)
        with Form(product) as form:
            form.soluong = 199
        self.assertEqual(product.soluong, 199)
        product.unlink()
        self.assertFalse(product.exists())

    def test_portal_cannot_read_sales_data(self):
        for model_name in ('hang', 'quanlybanhang.nhanvien', 'sanpham'):
            with self.subTest(model=model_name):
                self.assertIn(model_name, self.env.registry)
                with self.assertRaises(AccessError):
                    self.env[model_name].with_user(self.portal_user).search([])

    def test_internal_user_manages_sales_employees_from_form(self):
        self.assertIn('quanlybanhang.nhanvien', self.env.registry)
        with Form(self.env['quanlybanhang.nhanvien'].with_user(self.internal_user)) as form:
            form.tennv = 'Lê Việt Anh'
            form.manv = 1
            form.gioitinh = 'nam'
            form.sdt = '09865544333'
        employee = form.record
        self.assertEqual(employee.display_name, 'Lê Việt Anh')
        self.assertEqual(employee.sdt, '09865544333')
        with Form(employee) as form:
            form.sdt = '0901234567'
        self.assertEqual(employee.sdt, '0901234567')
        employee.unlink()
        self.assertFalse(employee.exists())

    def test_product_import_export_preserves_codes_and_values(self):
        self.assertIn('sanpham', self.env.registry)
        products = self.env['sanpham'].with_user(self.internal_user)
        imported = products.load(
            ['masp', 'tensp', 'soluong', 'giaban', 'mausac'],
            [['0007', 'Sản phẩm nhập', '12', '50000', 'do']],
        )
        self.assertFalse(imported.get('messages'), imported.get('messages'))
        product = products.browse(imported['ids'])
        exported = product.export_data(['masp', 'tensp', 'soluong', 'giaban'])
        self.assertEqual(exported['datas'], [['0007', 'Sản phẩm nhập', 12, 50000]])
