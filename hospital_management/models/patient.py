from odoo import models, fields, api
import random


class patient_management(models.Model):
    _name = 'patient.patient'
    _description = 'patient.patient'
    
    patient_id = fields.Char("ID")
    patient_fname = fields.Char("First Name")
    patient_lname = fields.Char("Last Name")
    patient_phone = fields.Char("Phone Number", required=True)
    patient_address = fields.Char("Address")
    patient_dayin = fields.Date("Start day")
    patient_dayout = fields.Date("Out day")
    patient_place = fields.Char("Hospital")