# -*- coding: utf-8 -*-

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class View(models.Model):

    _inherit = "ir.ui.view"

    visibility = fields.Selection(default='connected')
