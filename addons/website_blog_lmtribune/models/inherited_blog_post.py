# -*- coding: utf-8 -*-
from datetime import datetime
import requests
from lxml import html
from werkzeug import urls
import re
import base64
from odoo import api, models, fields, _, tools
from odoo.tools.mimetypes import guess_mimetype
import logging
_logger = logging.getLogger(__name__)


class InheritedBlogPost(models.Model):
    _inherit = "blog.post"

    is_lmtribune = fields.Boolean('Is from LMTribune', default=False)

    @api.model
    def lmtribune_scraper(self):

        website_id = self.env['website'].search([('lmtribune_username','!=',False),('lmtribune_password','!=',False),('lmtribune_blog_blog','!=',False)])
        if not website_id:
            return True

        homepage = requests.get('https://e.lmtribune.com/')
        tree = html.fromstring(homepage.text.encode('utf-8'), parser=html.HTMLParser(encoding='utf-8'))

        pdfs = self._parse_lmtribune_page_get_pdfs_dict(tree)
        _logger.info('PDFs found: %s' % pdfs)

        if pdfs:
            login_payload = {'token':'TOKEN', 'site':'lewisn04', 'login': website_id.lmtribune_username, 'password': website_id.lmtribune_password, 'sub': 'Submit' }
            login_url = 'https://e.lmtribune.com/login.php'
            base_pdf_url = 'https://e.lmtribune.com'

            with requests.Session() as s:
                r = s.post(login_url, data=login_payload)
                cookie = {'PHPSESSID': requests.utils.dict_from_cookiejar(s.cookies)['PHPSESSID']}
                _logger.info('logged into lmtribune, cookie: %s' % cookie)

                count_per_launch = 0
                for article_title, pdf_list in pdfs.items():

                    # if we already have this article - ignore it and continue
                    duplicates = self.search([('name','=',article_title),('is_lmtribune','=',True)])
                    if duplicates:
                        _logger.info('article already in odoo: %s' % duplicates)
                        if website_id.lmtribune_most_recent_only:
                            _logger.info('lmtribune_most_recent_only is ON - stopping')
                            break
                        else:
                            _logger.info('lmtribune_most_recent_only is OFF - continue')
                            continue

                    # create blog post
                    blog_post = self.create({
                        'website_id': website_id.id,
                        'is_lmtribune': True,
                        'name': article_title,
                        'blog_id': website_id.lmtribune_blog_blog.id,
                        'content': ''
                    })
                    _logger.info('blog post created, id/name: %s / %s' % (blog_post.id, blog_post.name))

                    content_cols = ''
                    for pdf_dict in pdf_list:

                        # download PDF image thumb and add attachment
                        pdf_img = requests.get('%s/%s' % (base_pdf_url, pdf_dict['img_src']), cookies=cookie)
                        image_base64 = base64.b64encode(pdf_img.content)
                        image_base64 = tools.image_process(image_base64, verify_resolution=True)
                        mimetype = guess_mimetype(base64.b64decode(image_base64))
                        pdf_img_attach = self.env['ir.attachment'].create({
                            'name': pdf_dict['text'] + '.jpg',
                            'mimetype': mimetype,
                            'datas': image_base64,
                            'res_model': self._name,
                            'res_id': blog_post.id,
                        })
                        pdf_img_attach.generate_access_token()
                        _logger.info('pdf thumb image attachment created, id: %s' % (pdf_img_attach.id))

                        # download PDF and add attachments
                        pdf_page = requests.get('%s/%s' % (base_pdf_url, pdf_dict['href']), cookies=cookie)
                        pdf_base64 = base64.b64encode(pdf_page.content)
                        pdf_attach = self.env['ir.attachment'].create({
                            'name': pdf_dict['text'] + '.pdf',
                            'type': 'binary',
                            'datas': pdf_base64,
                            'store_fname': pdf_dict['text'] + '.pdf',
                            'res_model': self._name,
                            'res_id': blog_post.id,
                            'mimetype': 'application/pdf'
                        })
                        _logger.info('pdf attachment created, id: %s' % (pdf_attach.id))
                        
                        image_url_with_token = '/web/image/%s?access_token=%s' % (pdf_img_attach.id, pdf_img_attach.access_token)
                        image_url = '/web/image/%s' % (pdf_img_attach.id)
                        content_cols += """
                            <div class="col-lg-6">
                                <a href="/web/content/%s"><img src="%s" class="img img-fluid mx-auto" alt="" loading="lazy" data-original-id="%s" data-original-src="%s" data-mimetype="image/jpeg"></a>
                                <p><a href="/web/content/%s" class="mb-2 btn btn-primary" data-original-title="" title="">Read now</a></p>
                            </div>
                        """ % (pdf_attach.id, image_url_with_token, pdf_img_attach.id, image_url, pdf_attach.id)                    

                    content_row = """
                        <div class="row">
                            %s
                        </div>
                    """ % content_cols

                    blog_post.write({
                        'content': content_row,
                        'is_published': True
                    })
                    count_per_launch += 1

                    if website_id.lmtribune_most_recent_only:
                        _logger.info('lmtribune_most_recent_only is ON - stopping')
                        break
                    elif count_per_launch >= website_id.lmtribune_count_per_launch:
                        _logger.info('lmtribune_count_per_launch is reached - stopping')
                        break

        return True


    def _parse_lmtribune_page_get_pdfs_dict(self, tree):

        pdfs = {}
        for pdf in tree.xpath("//div[contains(@class, 'pdf')]"):
            _logger.info('pdf found: %s' % html.tostring(pdf))
            prev_h3 = pdf.xpath("preceding::h3[1]")
            if prev_h3:
                prev_h3_text = prev_h3[0].text.strip()
                _logger.info('prev h3: %s' % prev_h3_text)
                a = pdf.find("a")
                _logger.info('a found: %s' % html.tostring(a))
                a_href = a.get('href')
                a_text = a.text_content()
                a_img = a.find("img")
                _logger.info('a img found: %s' % html.tostring(a_img))
                a_img_src = a_img.get('src')
                pdf_dict = {
                    'href': a_href,
                    'text': a_text,
                    'img_src': a_img_src
                }

                if prev_h3_text in pdfs:
                    pdfs[prev_h3_text].append(pdf_dict)
                else:
                    pdfs[prev_h3_text] = [pdf_dict]

        return pdfs