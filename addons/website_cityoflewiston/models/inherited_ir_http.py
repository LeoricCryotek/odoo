# -*- coding: utf-8 -*-

import logging
import werkzeug
import werkzeug.routing
import werkzeug.utils

from odoo import api, models
from odoo.http import request

_logger = logging.getLogger(__name__)

class Http(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _serve_page(cls):
        req_page = request.httprequest.path
        page_domain = [('url', '=', req_page)] + request.website.website_domain()

        published_domain = page_domain
        # specific page first
        page = request.env['website.page'].sudo().search(published_domain, order='website_id asc', limit=1)

        if page and request.website.cityoflewiston_website_pages_visibile_signed_in_only and request.website.is_public_user():
            redirect_query = werkzeug.urls.url_encode({
                'redirect': request.httprequest.url,
            })
            return request.redirect('/web/login?%s' % redirect_query, 303)


        return super(Http, cls)._serve_page()


