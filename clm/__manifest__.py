{
    'name': "CLM Contract Lifecycle Management",
    'version': '1.0',
    'depends': ['base'],
    'author': "Danny Santiago",
    'category': 'Services',
    'license': 'LGPL-3',
    'summary': 'Manage contracts from initiation to expiration or termination',
    'description': "Contract Lifecycle Management (CLM) Module for odoo",
    'application': True,
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
    ],
}
