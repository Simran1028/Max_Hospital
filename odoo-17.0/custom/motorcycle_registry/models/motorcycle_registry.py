from odoo import fields, models, _

class motorcycleregistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'motorcycle registry'
    _rec_name = 'first_name'
    
    certificate_title = fields.Binary('Certificate Title', required=True)
    current_mileage= fields.Float('Mileage')
    date_registry = fields.Date('Registry Date')
    first_name= fields.Char('First Name',required=True)
    last_name = fields.Char('Last Name',required=True)
    license_plate = fields.Char()
    registry_number=fields.Char('Registry Number',required=True)
    vehicle_image=fields.Image()