# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PaymentAcquirer(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('glcode', 'GL Code')], ondelete={'glcode': 'set default'})

    @api.depends('provider')
    def _compute_view_configuration_fields(self):
        """ Override of payment to hide the credentials page.

        :return: None
        """
        super()._compute_view_configuration_fields()
        self.filtered(lambda acq: acq.provider == 'glcode').show_credentials_page = False

    def _get_default_payment_method_id(self):
        self.ensure_one()
        if self.provider != 'glcode':
            return super()._get_default_payment_method_id()
        return self.env.ref('payment_test.payment_method_test').id
