{
    "name": "Website Gamification Dynamic Content",
    "version": "1.0",
    "category": "Website",
    "author": "Danny Santiago",
    "depends": ["website", "gamification"],
    "license": "LGPL-3",
    "application": "true",
    "data": [
        "security/ir.model.access.csv",
     #   "views/gamification_badge_view.xml",
     #   "static/src/xml/website_gamification_dynamic_content_templates.xml",
    ],
    'qweb': [
        'static/src/xml/website_gamification_dynamic_content_templates.xml',
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
