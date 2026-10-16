{
    'name': 'QLBanHang',

    'summary': 'Phần mềm Quản lý bán hàng trên odoo',

    'description': """
        Phần mềm Bán hàng - Hệ quản trị doanh nghiệp điện tử ERP
    """,

    'author': 'Than Ngoc Huan',
    'website': 'https://www.banhang.com.vn/',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/20.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Hệ thống quản lý bán hàng trên odoo',
    'version': '20.0.1.0.0',
    'license': 'LGPL-3',
    'application': True,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.access.csv',
        'views/quanlybanhang_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/quanlybanhang_demo.xml',
    ],
}
