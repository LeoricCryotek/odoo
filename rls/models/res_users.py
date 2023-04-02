from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    phone_ext = fields.Char(string='Phone Extension', related='partner_id.phone_ext', readonly=False)
    rls_manager = fields.Boolean(string='RLS Manager')
    rls_attorney = fields.Boolean(string='RLS Attorney')
    rls_administrator = fields.Boolean(string='RLS Administrator')

    def write(self, vals):
        if 'rls_manager' in vals and vals['rls_manager']:
            existing_manager = self.search([('rls_manager', '=', True), ('id', '!=', self.id)], limit=1)
            if existing_manager:
                raise UserError(_('There can only be one RLS Manager. %s is already assigned as the manager.') % existing_manager.name)
        return super(ResUsers, self).write(vals)
