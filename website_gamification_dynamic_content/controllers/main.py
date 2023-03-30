from odoo import http
from odoo.http import request

class WebsiteGamificationDynamicContent(http.Controller):
    @http.route('/gamification_dynamic_content/get_badges', type='json', auth='public', website=True)
    def get_badges(self, **kwargs):
        return request.env['gamification.badge'].search_read([], ['name', 'description'])
