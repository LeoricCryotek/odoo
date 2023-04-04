from odoo import api, fields, models


class RequestLegalServices(models.Model):
    _name = 'request.legal.services'
    _description = 'Request Legal Services'
    _inherit = ['mail.thread']

    name = fields.Char(string='Request', required=True, copy=False, default='New', tracking=True)
    nature_of_request = fields.Selection(selection=[('contract', 'Contract'),
                                                    ('dedication', 'Dedication'),
                                                    ('deed', 'Deed'),
                                                    ('easement', 'Easement'),
                                                    ('legal_opinion', 'Legal Opinion'),
                                                    ('ordinance', 'Ordinance'),
                                                    ('other', 'Other'),
                                                    ('resolution', 'Resolution'),
                                                    ('subpoena', 'Subpoena'),
                                                    ('vacation_of_r-o-w', 'Vacation of R-O-W')],
                                         string='Nature of Request', widget='selection', tracking=True)
    assigned_attorney_id = fields.Many2one('res.users', string='Attorney Assigned', domain="[(1, '=', 1)]", widget='selection', tracking=True)
    due_date = fields.Date(string='Due Date')
    active = fields.Boolean(default=True)

