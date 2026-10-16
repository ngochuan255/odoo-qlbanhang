from odoo.exceptions import AccessError
from odoo.tests import Form, TransactionCase, tagged
from odoo.tests.common import new_test_user


@tagged("post_install", "-at_install")
class TestQlNhanSu(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.internal_user = new_test_user(
            cls.env, login="ql_nhansu_internal", groups="base.group_user"
        )
        cls.portal_user = new_test_user(
            cls.env, login="ql_nhansu_portal", groups="base.group_portal"
        )

    def test_internal_user_manages_departments_from_form(self):
        self.assertIn("phong", self.env.registry)
        departments = self.env["phong"].with_user(self.internal_user)
        with Form(departments) as form:
            form.name = "Phòng kiểm thử"
            form.depid = 900
        department = form.record
        self.assertEqual(department.read(["name", "depid"])[0]["depid"], 900)
        with Form(department) as form:
            form.name = "Phòng đã cập nhật"
        self.assertEqual(department.name, "Phòng đã cập nhật")
        department.unlink()
        self.assertFalse(department.exists())

    def test_internal_user_manages_employees_from_form(self):
        self.assertIn("nhanvien", self.env.registry)
        employees = self.env["nhanvien"].with_user(self.internal_user)
        with Form(employees) as form:
            form.name = "Than Ngoc Huan"
            form.empid = 2023606980
            form.gender = "nam"
            form.phone = "0901234567"
        employee = form.record
        self.assertEqual(
            employee.read(["name", "empid", "gender", "phone"])[0],
            {
                "id": employee.id,
                "name": "Than Ngoc Huan",
                "empid": 2023606980,
                "gender": "nam",
                "phone": "0901234567",
            },
        )
        with Form(employee) as form:
            form.phone = "0907654321"
        self.assertEqual(employee.phone, "0907654321")
        employee.unlink()
        self.assertFalse(employee.exists())

    def test_portal_user_cannot_read_personnel_records(self):
        for model_name in ("phong", "nhanvien"):
            with self.subTest(model=model_name):
                self.assertIn(model_name, self.env.registry)
                with self.assertRaises(AccessError):
                    self.env[model_name].with_user(self.portal_user).search([])
