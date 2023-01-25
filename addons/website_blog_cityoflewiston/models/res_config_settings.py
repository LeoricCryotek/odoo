# -*- coding: utf-8 -*-

from odoo import api, fields, models, http

import logging
_logger = logging.getLogger(__name__)

class Website(models.Model):
    _inherit = "website"

    cityoflewiston_blog_visibile_signed_in_only = fields.Boolean('CityOfLewiston blog pages visible for signed-in users only')
    
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cityoflewiston_blog_visibile_signed_in_only = fields.Boolean(related='website_id.cityoflewiston_blog_visibile_signed_in_only', readonly=False)

