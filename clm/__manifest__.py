# clm/__manifest__.py

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
        'documents'
    ],
    'data': [
        'views/document_cancellation_terms_view.xml',
    ],
    'demo': [
    ],
}
