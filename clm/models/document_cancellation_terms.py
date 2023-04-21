# clm/models/document_cancellation_terms.py

from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class DocumentCancellationTerms(models.Model):
    _inherit = ['documents.document']

    cancellation_notice_enabled = fields.Boolean(string="Cancellation Notice")
    cancellation_notice = fields.Selection([
        ('30', '30 Days Written Notice'),
        ('60', '60 Days Written Notice'),
    ], string='Cancellation Notice')
    early_termination_fee = fields.Boolean(string="Early Termination Fee")
    early_termination_fee_amount = fields.Char(string="Early Termination Fee Amount")
    termination_for_cause = fields.Boolean(string="Termination for Cause")
    termination_upon_expiration = fields.Boolean(string="Termination upon Expiration")
    termination_for_non_payment = fields.Boolean(string="Termination for Non-payment")
    start_date = fields.Date(string='Start Date')
    termination_date = fields.Date(string='Termination Date', store=True)
    days_left_to_termination = fields.Integer(string='Days Left to Termination',
                                              compute='_compute_days_left_to_termination', store=True)
    days_left_to_cancel = fields.Integer(string='Days Left to Cancel', compute='_compute_days_left_to_cancel',
                                         store=True)
    term = fields.Selection([
        ('12', '12 Month'),
        ('24', '24 Month'),
        ('36', '36 Month'),
        ('48', '48 Month'),
        ('60', '60 Month'),
        ('other', 'Other'),
    ], string='Term')
    auto_renew = fields.Boolean(string='Auto Renew')
    cancellation_deadline = fields.Date(string='Cancellation Deadline', compute='_compute_cancellation_deadline')

    # ...
    @api.onchange('start_date', 'term')
    def _onchange_termination_date(self):
        for record in self:
            if record.start_date and record.term:
                if record.term != 'other':
                    months = int(record.term)
                    record.termination_date = record.start_date + relativedelta(months=months)
                else:
                    record.termination_date = False

    def _set_termination_date_readonly(self):
        for record in self:
            record.termination_date.readonly = record.term != 'other'

    @api.depends('termination_date', 'cancellation_notice')
    def _compute_cancellation_deadline(self):
        for record in self:
            if record.termination_date:
                if record.cancellation_notice == '30':
                    record.cancellation_deadline = record.termination_date - relativedelta(days=30)
                elif record.cancellation_notice == '60':
                    record.cancellation_deadline = record.termination_date - relativedelta(days=60)
                else:
                    record.cancellation_deadline = record.termination_date
            else:
                record.cancellation_deadline = False

    @api.depends('termination_date')
    def _compute_days_left_to_termination(self):
        for record in self:
            if record.termination_date:
                today = fields.Date.today()
                days_left_to_termination = (record.termination_date - today).days
                record.days_left_to_termination = days_left_to_termination - 1
            else:
                record.days_left_to_termination = 0

    @api.depends('cancellation_deadline')
    def _compute_days_left_to_cancel(self):
        for record in self:
            if record.cancellation_deadline:
                today = fields.Date.today()
                days_left_to_cancel = (record.cancellation_deadline - today).days
                record.days_left_to_cancel = days_left_to_cancel - 1
            else:
                record.days_left_to_cancel = 0

    @api.model
    def update_days_left(self):
        today = fields.Date.today()
        docs = self.search([])

        # Filter out records with null or zero values for the days_left_to_termination and days_left_to_cancel fields
        docs = docs.filtered(lambda d: d.days_left_to_termination and d.days_left_to_cancel)

        for doc in docs:
            days_left_to_termination = (doc.deadline_to_termination - today).days
            days_left_to_cancel = (doc.deadline_to_cancel - today).days
            doc.write({
                'days_left_to_termination': days_left_to_termination,
                'days_left_to_cancel': days_left_to_cancel,
            })
    # Add other fields for cancellation terms as needed
