from odoo import fields, models

class GamificationBadge(models.Model):
    _inherit = "gamification.badge"

    website_published = fields.Boolean('Published on Website', default=False)
