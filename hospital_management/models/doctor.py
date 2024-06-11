from odoo import models, fields, api
import random

class doctor_management(models.Model):
    _name = 'doctor.doctor'
    _description = 'doctor.doctor'

    doctor_fname = fields.Char("First Name", required=True)
    doctor_lname = fields.Char("Last Name", required=True)
    address_doc = fields.Char("Address")
    doctor_id = fields.Char("DocID")
    doc_phone_number = fields.Char("Phone Number")
    doc_workplace = fields.Char("Workplace")