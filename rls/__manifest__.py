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
        'base_setup',
        'sales_team',
        'mail',
        'calendar',
        'resource',
        'utm',
        'web_tour',
        'contacts',
        'digest',
        'phone_validation',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/actions.xml',
        'views/requests.xml',
        'views/rls_dashboard.xml',
        'views/res_config_settings_views.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}