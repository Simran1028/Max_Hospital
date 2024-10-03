# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class max_odoo_inheritance(models.Model):
#     _name = 'max_odoo_inheritance.max_odoo_inheritance'
#     _description = 'max_odoo_inheritance.max_odoo_inheritance'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

