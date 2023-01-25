# -*- coding: utf-8 -*-

import werkzeug

from odoo import http, fields
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class InheritedWebsiteSale(WebsiteSale):

    def _check_cityoflewiston_sale_visibility(self):
        if request.website.cityoflewiston_sale_visibile_signed_in_only and request.website.is_public_user():
            redirect_query = werkzeug.urls.url_encode({
                'redirect': request.httprequest.url,
            })
            return request.redirect('/web/login?%s' % redirect_query, 303)
        else:
            return False

    @http.route()
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):

        res = self._check_cityoflewiston_sale_visibility()
        if res:
            return res

        return super().shop(page=page, category=category, search=search, min_price=min_price, max_price=max_price, ppg=ppg, **post)

    @http.route()
    def product(self, product, category='', search='', **kwargs):
        res = self._check_cityoflewiston_sale_visibility()
        if res:
            return res

        return super().product(product, category=category, search=search, **kwargs)

    @http.route()
    def old_product(self, product, category='', search='', **kwargs):
        res = self._check_cityoflewiston_sale_visibility()
        if res:
            return res

        return super().old_product(product, category=category, search=search, **kwargs)

    @http.route()
    def cart(self, access_token=None, revive='', **post):
        res = self._check_cityoflewiston_sale_visibility()
        if res:
            return res

        return super().cart(access_token=access_token, revive=revive, **post)

    @http.route()
    def checkout(self, **post):
        res = self._check_cityoflewiston_sale_visibility()
        if res:
            return res

        return super().checkout(**post)

