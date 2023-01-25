# -*- coding: utf-8 -*-
import logging

from odoo import api, fields, models

logger = logging.getLogger(__name__)

class Website(models.Model):

    _inherit = "website"

    def set_visibility_connected_for_all_pages(self):

        for website in self:
            domain_static = website.website_domain()
            self.env['website.page'].sudo().search(domain_static).write({'visibility': 'connected'})

    def set_visibility_all_for_all_pages(self):

        for website in self:
            domain_static = website.website_domain()
            self.env['website.page'].sudo().search(domain_static).write({'visibility': ''})
