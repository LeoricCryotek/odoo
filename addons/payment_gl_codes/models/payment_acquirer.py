# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('gl_codes', 'GL Codes')], ondelete={'gl_codes': 'set default'})

    @api.depends('provider')
    def _compute_view_configuration_fields(self):

        super()._compute_view_configuration_fields()
        # bypass the credentials page
        self.filtered(lambda acq: acq.provider == 'gl_codes').show_credentials_page = False

    def _get_default_payment_method_id(self):
        self.ensure_one()
        if self.provider != 'gl_codes':
            return super()._get_default_payment_method_id()
        return self.env.ref('payment_gl_codes.payment_method_gl_codes').id
