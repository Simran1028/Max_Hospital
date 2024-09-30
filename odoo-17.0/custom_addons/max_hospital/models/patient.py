from datetime import date
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name="hospital.patient"
    _inherit=['mail.thread','mail.activity.mixin']
    _description="Hospital Patients"

    name=fields.Char(string='Name',required=True,tracking=True)
    age=fields.Integer(string='Age',compute='_compute_age',tracking=True, placeholder='Choose D.O.B')
    date_of_birth=fields.Date(string='D.O.B',tracking=True)
    gender=fields.Selection([
        ('male','MALE'),
        ('female','FEMALE'),
        ('other','OTHER'),
    ],required=True,default='male',tracking=True)
    ref=fields.Char(string="Reference")
    note=fields.Text(string='Description',tracking=True)
    active=fields.Boolean(string="Active",default=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
       for rec in self:
           today=date.today()
           if rec.date_of_birth:
               rec.age = today.year - rec.date_of_birth.year
           else:
               rec.age=0   