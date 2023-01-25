# -*- coding: utf-8 -*-

from odoo import _, fields, models

class PaymentToken(models.Model):
    _inherit = 'payment.token'

    gl_code = fields.Char(string="GL Code", readonly=True)
