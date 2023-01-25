# -*- coding: utf-8 -*-
{
    'name': 'GL Codes Payment Acquirer',
    'version': '15.0.1',
    'category': 'Accounting/Payment Acquirers',
    'description': """GL codes payment acquirer""",
    'depends': ['payment', 'sale', 'website_sale'],
    'data': [

        # model views
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
        'views/account_payment_views.xml',
        'views/payment_transaction_views.xml',
        'views/payment_token_views.xml',

        # report views
        'views/sale_order_report_templates.xml',
        'views/report_payment_receipt_templates.xml',

        # website templates
        'views/payment_gl_codes_templates.xml',

        # customer portal templates
        'views/sale_portal_templates.xml',

        # data
        'data/payment_acquirer_data.xml',

    ],
    'uninstall_hook': 'uninstall_hook',
    'assets': {
        'web.assets_frontend': [
            'payment_gl_codes/static/src/js/**/*',
        ],
    },
    'license': 'LGPL-3',
}
