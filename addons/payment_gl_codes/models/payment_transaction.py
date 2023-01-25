# -*- coding: utf-8 -*-

from odoo import _, api, models, fields
from odoo.exceptions import ValidationError

from odoo.addons.payment import utils as payment_utils

class PaymentTransaction(models.Model):
    _inherit = 'payment.transaction'

    gl_code = fields.Char(string='GL Code', help="GL Code used to confirm this transaction via GL Codes payment acquirer.", readonly=True)

    def _send_payment_request(self):

        super()._send_payment_request()
        if self.provider != 'gl_codes':
            return

        # taking GL code from payment token
        self._handle_feedback_data('gl_codes', {
            'reference': self.reference, 
            'gl_code': self.token_id.gl_code
        })

    @api.model
    def _get_tx_from_feedback_data(self, provider, data):

        tx = super()._get_tx_from_feedback_data(provider, data)
        if provider != 'gl_codes':
            return tx

        reference = data.get('reference')
        tx = self.search([('reference', '=', reference), ('provider', '=', 'gl_codes')])
        if not tx:
            raise ValidationError(
                "GL Codes: " + _("No transaction found matching reference %s.", reference)
            )
        return tx

    def _process_feedback_data(self, data):

        super()._process_feedback_data(data)
        if self.provider != "gl_codes":
            return

        self.write({'gl_code': data['gl_code']})
        self.sale_order_ids.write({'gl_code': data['gl_code']})

        self._set_done()  # confirm transaction
        if self.tokenize:
            token = self.env['payment.token'].create({
                'acquirer_id': self.acquirer_id.id,
                'name': payment_utils.build_token_name(payment_details_short=data['gl_code']),
                'partner_id': self.partner_id.id,
                'gl_code': data['gl_code'],
                'acquirer_ref': 'GL codes acquirer reference',
                'verified': True,
            })
            self.token_id = token.id
