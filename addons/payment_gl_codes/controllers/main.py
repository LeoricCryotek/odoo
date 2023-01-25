from odoo import http
from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale

class WebsiteSaleProductComparison(WebsiteSale):

    def _get_mandatory_fields_billing(self, country_id=False):
        req = ["name", "email"]
        return req

    def _get_mandatory_fields_shipping(self, country_id=False):
        req = ["name"]
        return req


class PaymentGLCodesController(http.Controller):

    @http.route('/payment/gl_codes/simulate_payment', type='json', auth='public')
    def gl_codes_simulate_payment(self, reference, customer_input):

        request.env['payment.transaction'].sudo()._handle_feedback_data('gl_codes', {
            'reference': reference,
            'gl_code': customer_input,
        })
