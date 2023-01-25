# -*- coding: utf-8 -*-

import werkzeug

from odoo import http, fields
from odoo.http import request
from odoo.addons.website.controllers.main import Website

class InheritedWebsite(Website):

    def _check_cityoflewiston_website_visibility(self):
        if request.website.cityoflewiston_website_pages_visibile_signed_in_only and request.website.is_public_user():
            redirect_query = werkzeug.urls.url_encode({
                'redirect': request.httprequest.url,
            })
            return request.redirect('/web/login?%s' % redirect_query, 303)
        else:
            return False

    @http.route()
    def index(self, **kw):

        res = self._check_cityoflewiston_website_visibility()
        if res:
            return res

        return super().index(**kw)

    @http.route()
    def pages_list(self, page=1, search='', **kw):

        res = self._check_cityoflewiston_website_visibility()
        if res:
            return res

        return super().pages_list(page=page, search=search, **kw)

    @http.route()
    def hybrid_list(self, page=1, search='', search_type='all', **kw):

        res = self._check_cityoflewiston_website_visibility()
        if res:
            return res

        return super().hybrid_list(page=page, search=search, search_type=search_type, **kw)

