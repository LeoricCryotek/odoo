# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    # taking GL code from payment.transaction connected to this payment
    gl_code = fields.Char(string='GL Code', related='payment_transaction_id.gl_code')

