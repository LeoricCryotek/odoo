# -*- coding: utf-8 -*-

import werkzeug

from odoo import http, fields
from odoo.http import request
from odoo.addons.website_event.controllers.main import WebsiteEventController

class InheritedWebsiteEvent(WebsiteEventController):

    def _check_cityoflewiston_event_visibility(self):
        if request.website.cityoflewiston_event_visibile_signed_in_only and request.website.is_public_user():
            redirect_query = werkzeug.urls.url_encode({
                'redirect': request.httprequest.url,
            })
            return request.redirect('/web/login?%s' % redirect_query, 303)
        else:
            return False

    @http.route()
    def events(self, page=1, **searches):

        res = self._check_cityoflewiston_event_visibility()
        if res:
            return res

        return super().events(page=page, **searches)

    @http.route()
    def event_page(self, event, page, **post):
        res = self._check_cityoflewiston_event_visibility()
        if res:
            return res

        return super().event_page(event, page, **post)

    @http.route()
    def event(self, event, **post):
        res = self._check_cityoflewiston_event_visibility()
        if res:
            return res

        return super().event(event, **post)

    @http.route()
    def event_register(self, event, **post):
        res = self._check_cityoflewiston_event_visibility()
        if res:
            return res

        return super().event_register(event, **post)

