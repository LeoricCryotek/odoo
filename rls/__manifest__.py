# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Request for Legal Services',
    'version': '1.2',
    'author': 'Danny Santiago',
    'category': 'Services/Legal',
    'website':'https://home.cityoflewiston.org',
    'sequence': 15,
    'license': 'LGPL-3',
    'summary': 'Track request for legal services and their status. ',
    'description': "The best tool around for Legal Service Requests",
    'depends': [
        'mail',
        'calendar',
        'web',
        'crm',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/request_legal_services.xml',
        'views/ir_cron_data.xml',
        'views/request_legal_services.xml',
        'views/rls_dashboard_view.xml',
        'actions/actions.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
