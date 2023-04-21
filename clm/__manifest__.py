# clm/__manifest__.py

{
    'name': "CLM Contract Lifecycle Management",
    'version': '1.0',
    'author': "Danny Santiago",
    'category': 'Services',
    'license': 'LGPL-3',
    'summary': 'Manage contracts from initiation to expiration or termination',
    'description': "Contract Lifecycle Management (CLM) Module for odoo",
    'depends': ['base',
                'documents',
    ],
    'data': [
        'views/document_cancellation_terms_view.xml',
        'views/form_menu_view.xml',
        'views/clm_report_filters.xml',
        'data/scheduled_action.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False
}
