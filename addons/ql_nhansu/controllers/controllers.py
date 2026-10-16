# from odoo import http


# class QlNhansu(http.Controller):
#     @http.route('/ql_nhansu/ql_nhansu', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ql_nhansu/ql_nhansu/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ql_nhansu.listing', {
#             'root': '/ql_nhansu/ql_nhansu',
#             'objects': http.request.env['ql_nhansu.ql_nhansu'].search([]),
#         })

#     @http.route('/ql_nhansu/ql_nhansu/objects/<model("ql_nhansu.ql_nhansu"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ql_nhansu.object', {
#             'object': obj
#         })
