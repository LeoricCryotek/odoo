# clm/models/document.py

from odoo import models, fields

class Document(models.Model):
    _inherit = 'documents.document'

    # Add the new fields for cancellation terms checkboxes
    written_notice_30 = fields.Boolean("30 Days Written Notice")
    written_notice_60 = fields.Boolean("60 Days Written Notice")
    early_termination_fee = fields.Boolean("Early Termination Fee")
    termination_for_convenience = fields.Boolean("Termination for Convenience")
    termination_for_cause = fields.Boolean("Termination for Cause")
    termination_upon_expiration = fields.Boolean("Termination upon Expiration")
    termination_upon_bankruptcy = fields.Boolean("Termination upon Bankruptcy or Insolvency")
    termination_for_non_payment = fields.Boolean("Termination for Non-payment")
    termination_upon_change_of_control = fields.Boolean("Termination upon Change of Control")
    termination_for_force_majeure = fields.Boolean("Termination for Force Majeure")
    mutual_termination = fields.Boolean("Mutual Termination")
