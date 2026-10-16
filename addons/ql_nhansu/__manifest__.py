# -*- coding: utf-8 -*-
{
    'name': 'Than Ngoc Huan - 2023606980',
    'summary': 'Thực hành lập trình Odoo',
    'description': """
        Học lập trình Odoo - Hệ quản trị doanh nghiệp điện tử ERP
    """,
    'author': 'Than Ngoc Huan',
    'website': 'https://www.google.com.vn/',
    'category': 'Hệ thống thông tin',
    'version': '20.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
