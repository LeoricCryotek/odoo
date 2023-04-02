from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_council = fields.Boolean(string='Is Outside Council', default=False)

    def action_set_council(self):
        for partner in self:
            partner.is_council = True

    def action_unset_council(self):
        for partner in self:
            partner.is_council = False
