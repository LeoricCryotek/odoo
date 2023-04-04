from odoo import api, fields, models


class RequestLegalServices(models.Model):
    _name = 'request.legal.services'
    _description = 'Request Legal Services'
    _inherit = ['mail.thread']

    #name = fields.Char(required=True, string='Name', widget='Text', tracking=True)
    #nature_of_request = fields.Selection(selection=[('contract', 'Contract'),
                                                  #  ('dedication', 'Dedication'),
                                                  #  ('deed', 'Deed'),
                                                  #  ('easement', 'Easement'),
                                                  #  ('legal_opinion', 'Legal Opinion'),
                                                  #  ('ordinance', 'Ordinance'),
                                                  #  ('other', 'Other'),
                                                  #  ('resolution', 'Resolution'),
                                                  #  ('subpoena', 'Subpoena'),
                                                  #  ('vacation_of_r-o-w', 'Vacation of R-O-W')],
                                        # string='Nature of Request', widget='selection', tracking=True)
