
from odoo import api, fields, models

class CancelAppointments(models.TransientModel):
    _name="cancel.appointments"
    _description="Cancel Appointments"

    
    appointment_id=fields.Many2one('hospital.appointment',string='Appointment')
    reason=fields.Text(string='Reason')
    def action_cancel(self):
        return