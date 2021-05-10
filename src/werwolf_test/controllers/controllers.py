# -*- coding: utf-8 -*-
from odoo import http

# class WerwolfTest(http.Controller):
#     @http.route('/werwolf_test/werwolf_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/werwolf_test/werwolf_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('werwolf_test.listing', {
#             'root': '/werwolf_test/werwolf_test',
#             'objects': http.request.env['werwolf_test.werwolf_test'].search([]),
#         })

#     @http.route('/werwolf_test/werwolf_test/objects/<model("werwolf_test.werwolf_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('werwolf_test.object', {
#             'object': obj
#         })