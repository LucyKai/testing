# -*- coding: utf-8 -*-
{
    'name': "custom-module",

    'summary': """
        Testing about Odoo""",

    'description': """
        Testing about Odoo
    """,

    'author': "Lwin Mar Win",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'author': "Lwin Mar Win",
    'website': "https://www.linkedin.com/in/hilar-ak/",
    'category': "Generic Modules/Human Resources",
    'version': "12.0.1.0.0",

    # any module necessary for this one to work correctly
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
