# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class SaleOrder(models.Model):
    _inherit = "sale.order"

    gl_code = fields.Char(string='GL Code', help="GL Code used to confirm this order via GL Codes payment acquirer.", readonly=True)
