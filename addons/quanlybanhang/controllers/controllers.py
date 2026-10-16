# from odoo import http


# class Quanlybanhang(http.Controller):
#     @http.route('/quanlybanhang/quanlybanhang', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quanlybanhang/quanlybanhang/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('quanlybanhang.listing', {
#             'root': '/quanlybanhang/quanlybanhang',
#             'objects': http.request.env['quanlybanhang.quanlybanhang'].search([]),
#         })

#     @http.route('/quanlybanhang/quanlybanhang/objects/<model("quanlybanhang.quanlybanhang"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quanlybanhang.object', {
#             'object': obj
#         })
