# clm/__manifest__.py

{
    'name': "CLM Contract Lifecycle Management",
    'version': '1.0',
    'author': "Danny Santiago",
    'category': 'Services',
    'license': 'LGPL-3',
    'summary': 'Manage contracts from initiation to expiration or termination',
    'description': "Contract Lifecycle Management (CLM) Module for odoo",
    'application': True,
    'depends': ['base',
                'documents',
    ],
    'data': [
        'views/document_cancellation_terms_view.xml',
    ],
    'data': [
        # Add your other XML files here
        'data/scheduled_action.xml',
    ],
    'installable': True,
}
