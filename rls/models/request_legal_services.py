from odoo import api, fields, models

class RequestLegalServices(models.Model):
    _name = 'request.legal.services'
    _description = 'Request Legal Services'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, string='Name', tracking=True)
    request_type = fields.Many2one('request.type', string='Request Type', tracking=True)
    department_id = fields.Many2one('hr.department', string='Department', tracking=True)
    division_id = fields.Many2one('hr.department.division', string='Division', tracking=True)
    attorney_assigned = fields.Many2one('res.users', string='Assigned Attorney', tracking=True)
    legal_team = fields.Many2one('res.users', string='Legal Team', tracking=True)
    outside_counsel = fields.Many2one('res.partner', string='Outside Counsel', tracking=True)
    phone_ext = fields.Char(related='create_uid.phone', string='Phone Extension', readonly=True)
    due_date = fields.Date(string='Due Date', tracking=True)
    days_until_due = fields.Integer(string='Days Until Due', compute='_compute_days_until_due', store=True)
    nature_of_request = fields.Selection(selection=[], string='Nature of Request', tracking=True)

    @api.depends('due_date')
    def _compute_days_until_due(self):
        for record in self:
            if record.due_date:
                record.days_until_due = (record.due_date - fields.Date.today()).days
            else:
                record.days_until_due = 0

    @api.onchange('department_id')
    def _onchange_department_id(self):
        self.division_id = False

    @api.model
    def create(self, vals):
        res = super(RequestLegalServices, self).create(vals)
        res.message_subscribe(partner_ids=res.legal_team.partner_id.ids)
        return res
