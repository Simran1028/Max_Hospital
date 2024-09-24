from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name="hospital.patient"
    _inherit=['mail.thread','mail.activity.mixin']
    _description="Hospital Patients"

    name=fields.Char(string='Name',required=True,tracking=True)
    age=fields.Integer(string='Age',tracking=True)
    date_of_birth=fields.Date(string='D.O.B',tracking=True)
    gender=fields.Selection([
        ('male','MALE'),
        ('female','FEMALE'),
        ('other','OTHER'),
    ],required=True,default='male',tracking=True)
    note=fields.Text(string='Description',tracking=True)
    active=fields.Boolean(string="Active",default=True)