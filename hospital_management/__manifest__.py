# -*- coding: utf-8 -*-
{
    'name': "hospital_management",

    'summary': "This is an addon for testing purpose",

    'description': """
        I will try to create a module fo myself
    """,

    'author': "Valley Campus Saigon",
    'website': "https://www.valleycampus.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}

