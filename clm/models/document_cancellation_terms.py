# clm/models/document_cancellation_terms.py

from odoo import api, fields, models

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
    term = fields.Selection([
        ('12', '12 Month'),
        ('24', '24 Month'),
        ('36', '36 Month'),
        ('48', '48 Month'),
        ('60', '60 Month'),
    ], string="Term")
    start_date = fields.Date(string="Start Date")
    termination_date = fields.Date(string="Termination Date")
    days_left = fields.Integer(string="Days Left")
    # Add other fields for cancellation terms as needed
