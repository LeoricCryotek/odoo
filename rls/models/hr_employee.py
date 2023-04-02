from odoo import fields, models

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    user_id = fields.Many2one(
        'res.users', string='User',
        help='User related to this employee',
        compute='_compute_user_id', store=True,
    )

    def _compute_user_id(self):
        for employee in self:
            user = self.env['res.users'].search([('employee_id', '=', employee.id)], limit=1)
            employee.user_id = user.id if user else False
