# -*- coding: utf-8 -*-

from odoo import api, fields, models, http

import logging
_logger = logging.getLogger(__name__)

class Website(models.Model):
    _inherit = "website"

    cityoflewiston_sale_visibile_signed_in_only = fields.Boolean('CityOfLewiston shop pages visible for signed-in users only')
    
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cityoflewiston_sale_visibile_signed_in_only = fields.Boolean(related='website_id.cityoflewiston_sale_visibile_signed_in_only', readonly=False)

