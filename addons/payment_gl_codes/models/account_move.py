# -*- coding: utf-8 -*-

from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    gl_code = fields.Char(string='Sales Order GL Code', compute='_compute_gl_code')

    def _compute_gl_code(self):
        # invoice supports having lines from different sales orders, but we assume it's connected to only one sales order, so we're taking the first one we find
        for move in self:
            res = False
            for line in move.line_ids:
                if line.sale_line_ids:
                    for sl in line.sale_line_ids:
                        if sl.order_id.gl_code:
                            res = sl.order_id.gl_code
                            break
            
            move.gl_code = res
