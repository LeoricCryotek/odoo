# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Real Estate Manager',
    'version': '1.2',
    'author': 'Danny Santiago',
    'category': 'Sales/estate',
    'sequence': 15,
    'license': 'LGPL-3',
    'summary': 'Track leads and close opportunities for Real Estate ',
    'description': "The Real Estate Tool to Rule",
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
    ],
    'demo': [
        'data/crm_team_demo.xml',
        'data/mail_activity_demo.xml',
        'data/crm_lead_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}