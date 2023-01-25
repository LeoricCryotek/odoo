odoo.define('payment_gl_codes.payment_form', require => {
    'use strict';

    const checkoutForm = require('payment.checkout_form');
    const manageForm = require('payment.manage_form');

    const paymentGLCodesMixin = {

        _processDirectPayment: function (provider, acquirerId, processingValues) {
            if (provider !== 'gl_codes') {
                return this._super(...arguments);
            }

            const customerInput = document.getElementById('customer_input').value;
            return this._rpc({
                route: '/payment/gl_codes/simulate_payment',
                params: {
                    'reference': processingValues.reference,
                    'customer_input': customerInput,
                },
            }).then(() => {
                window.location = '/payment/status';
            });
        },

        _prepareInlineForm: function (provider, paymentOptionId, flow) {
            if (provider !== 'gl_codes') {
                return this._super(...arguments);
            } else if (flow === 'token') {
                return Promise.resolve();
            }
            this._setPaymentFlow('direct');
            return Promise.resolve()
        },
    };
    checkoutForm.include(paymentGLCodesMixin);
    manageForm.include(paymentGLCodesMixin);
});
