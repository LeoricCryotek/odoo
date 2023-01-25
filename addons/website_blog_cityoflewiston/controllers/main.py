# -*- coding: utf-8 -*-

import werkzeug

from odoo import http, fields
from odoo.http import request
from odoo.addons.website_blog.controllers.main import WebsiteBlog

import logging
_logger = logging.getLogger(__name__)

class InheritedWebsiteBlog(WebsiteBlog):

    def _check_cityoflewiston_blog_visibility(self):
        if request.website.cityoflewiston_blog_visibile_signed_in_only and request.website.is_public_user():
            redirect_query = werkzeug.urls.url_encode({
                'redirect': request.httprequest.url,
            })
            return request.redirect('/web/login?%s' % redirect_query, 303)
        else:
            return False


    @http.route()
    def blog(self, blog=None, tag=None, page=1, search=None, **opt):
        res = self._check_cityoflewiston_blog_visibility()
        if res:
            return res

        return super().blog(blog=blog, tag=tag, page=page, search=search, **opt)

    @http.route()
    def blog_feed(self, blog, limit='15', **kwargs):

        res = self._check_cityoflewiston_blog_visibility()
        if res:
            return res

        return super().blog_feed(blog=blog, limit=limit, **kwargs)

    @http.route()
    def old_blog_post(self, blog, blog_post, tag_id=None, page=1, enable_editor=None, **post):
        res = self._check_cityoflewiston_blog_visibility()
        if res:
            return res

        return super().old_blog_post(blog, blog_post, tag_id=tag_id, page=page, enable_editor=enable_editor, **post)

    @http.route()
    def blog_post(self, blog, blog_post, tag_id=None, page=1, enable_editor=None, **post):
        res = self._check_cityoflewiston_blog_visibility()
        if res:
            return res

        return super().blog_post(blog, blog_post, tag_id=tag_id, page=page, enable_editor=enable_editor, **post)
