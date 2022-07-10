# -*- coding: utf-8 -*-
from odoo import http

# class MethodSoRma(http.Controller):
#     @http.route('/method_so_rma/method_so_rma/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_so_rma/method_so_rma/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_so_rma.listing', {
#             'root': '/method_so_rma/method_so_rma',
#             'objects': http.request.env['method_so_rma.method_so_rma'].search([]),
#         })

#     @http.route('/method_so_rma/method_so_rma/objects/<model("method_so_rma.method_so_rma"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_so_rma.object', {
#             'object': obj
#         })