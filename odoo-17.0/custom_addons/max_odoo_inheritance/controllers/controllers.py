# -*- coding: utf-8 -*-
# from odoo import http


# class MaxOdooInheritance(http.Controller):
#     @http.route('/max_odoo_inheritance/max_odoo_inheritance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/max_odoo_inheritance/max_odoo_inheritance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('max_odoo_inheritance.listing', {
#             'root': '/max_odoo_inheritance/max_odoo_inheritance',
#             'objects': http.request.env['max_odoo_inheritance.max_odoo_inheritance'].search([]),
#         })

#     @http.route('/max_odoo_inheritance/max_odoo_inheritance/objects/<model("max_odoo_inheritance.max_odoo_inheritance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('max_odoo_inheritance.object', {
#             'object': obj
#         })

