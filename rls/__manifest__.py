# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Request for Legal Services',
    'version': '1.2',
    'author': 'Danny Santiago',
    'category': 'Productivity/legal',
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
        'views/requests.xml'
    ],
    'demo': [
#        'data/crm_team_demo.xml',
#        'data/mail_activity_demo.xml',
#        'data/crm_lead_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False
}