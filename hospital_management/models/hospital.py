from odoo import models, fields, api
import random

class hospital_management(models.Model):
    _name = 'hospital_management.hospital_management'
    _description = 'hospital_management.hospital_management'

    branch_name = fields.Char("Branch Name", required=True)  
    address_hos = fields.Char("Address", required=True)
    phone_number = fields.Char("Phone Number", required=True)
    description_hos = fields.Text("Description")