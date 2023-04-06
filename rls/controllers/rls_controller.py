from odoo import http
from odoo.http import request

class RLSController(http.Controller):

    @http.route('/rls/submit_form', type='http', auth='public', website=True, csrf=False, methods=['POST'])
    def submit_form(self, **post):
        # Your custom code to handle form data
        # e.g., create a new record, send an email, etc.
        # You can access form data using post.get('field_name')

        # Redirect user to a specific page after form submission
        return request.redirect('/success_page')
