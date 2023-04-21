# clm/models/document_cancellation_terms.py

from odoo import api, fields, models
from dateutil.relativedelta import relativedelta


class DocumentCancellationTerms(models.Model):
    _inherit = 'documents.document'

    written_notice_30 = fields.Boolean(string="30 Days Written Notice")
    written_notice_60 = fields.Boolean(string="60 Days Written Notice")
    early_termination_fee = fields.Boolean(string="Early Termination Fee")
    termination_for_convenience = fields.Boolean(string="Termination for Convenience")
    termination_for_cause = fields.Boolean(string="Termination for Cause")
    termination_upon_expiration = fields.Boolean(string="Termination upon Expiration")
    termination_upon_bankruptcy = fields.Boolean(string="Termination upon Bankruptcy or Insolvency")
    termination_for_non_payment = fields.Boolean(string="Termination for Non-payment")
    termination_upon_change_of_control = fields.Boolean(string="Termination upon Change of Control")
    termination_for_force_majeure = fields.Boolean(string="Termination for Force Majeure")
    mutual_termination = fields.Boolean(string="Mutual Termination")
    start_date = fields.Date(string='Start Date')
    termination_date = fields.Date(string='Termination Date', store=True)
    days_left = fields.Integer(string='Days Left', compute='_compute_days_left', store=True)
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

    @api.depends('termination_date')
    def _compute_days_left(self):
        for record in self:
            if record.termination_date:
                today = fields.Date.today()
                days_left = (record.termination_date - today).days
                record.days_left = days_left - 1
            else:
                record.days_left = 0

    @api.depends('termination_date', 'written_notice_30', 'written_notice_60')
    def _compute_cancellation_deadline(self):
        for record in self:
            if record.termination_date:
                if record.written_notice_30:
                    record.cancellation_deadline = record.termination_date - relativedelta(days=30)
                elif record.written_notice_60:
                    record.cancellation_deadline = record.termination_date - relativedelta(days=60)
                else:
                    record.cancellation_deadline = record.termination_date
            else:
                record.cancellation_deadline = False

    # Add other fields for cancellation terms as needed
