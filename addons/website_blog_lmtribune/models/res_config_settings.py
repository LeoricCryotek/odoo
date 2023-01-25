# -*- coding: utf-8 -*-

from odoo import api, fields, models, http
from odoo.exceptions import UserError, AccessDenied, AccessError, MissingError
from odoo.tools.translate import _
from odoo.http import request
import werkzeug
import werkzeug.exceptions
import werkzeug.routing
import werkzeug.utils

import logging
_logger = logging.getLogger(__name__)

class Website(models.Model):
    _inherit = "website"

    lmtribune_username = fields.Char('LMTribune username')
    lmtribune_password = fields.Char('LMTribune password')
    lmtribune_blog_blog = fields.Many2one('blog.blog', string='LMTribune Blog')
    lmtribune_most_recent_only = fields.Boolean(string='LMTribune Get Most Recent Only', default=True)
    lmtribune_count_per_launch = fields.Integer(string='LMTribune Count Per Launch', default=1)
    
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    lmtribune_username = fields.Char(related='website_id.lmtribune_username', readonly=False)
    lmtribune_password = fields.Char(related='website_id.lmtribune_password', readonly=False)
    lmtribune_blog_blog = fields.Many2one(related='website_id.lmtribune_blog_blog', readonly=False)
    lmtribune_most_recent_only = fields.Boolean(related='website_id.lmtribune_most_recent_only', readonly=False)
    lmtribune_count_per_launch = fields.Integer(related='website_id.lmtribune_count_per_launch', readonly=False)

