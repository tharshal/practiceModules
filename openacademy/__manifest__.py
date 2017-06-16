# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Modules for odoo""",

    'description': """Courses Names and their Description
    """,

    'author': "techspawn",
    'website': "harshal@techspawn.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/openacademy.xml',
        'views/openacademyMyview.xml',
        'views/openacaSession.xml',
        #'views/partner.xml'
        #'demo/demo.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
