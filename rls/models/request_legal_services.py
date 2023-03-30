# -*- coding: utf-8 -*-
from odoo import api, fields, models

class RequestLegalServices(models.Model):
    _name = "legal.requests"
    _description = "Legal Requests"

    task_name = fields.Char(string="Account Name", required=True, index='trigram', tracking=True)
#    rls = fields.Interger()
#    due_date = datetime(required=True,)
#    days_until_due = fields()
#    priority =  fields.Selection()
    notes = fields.Text(string='Description')
#    reminder = fields.Selection()
#    requested by = field.Char(related="res.partner", required=True,)
#    department = resu_user.department(required=True,)
#    division = res.user.division(required=True,)
#    phone_ext = res.user.phone(required=True,)
#    position_title = res.user.title(required=True,)
#    request_date = datetime
#    nature_of_request = fields.Selection()
#    requested_due_date = datetime
#    completed_date = datetime
#    attorney_assigned = fields.Selection()
#    outside_council_assigned = fields.Selection()


