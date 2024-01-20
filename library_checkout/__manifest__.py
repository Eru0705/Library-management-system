# -*- coding: utf-8 -*-
{
    'name': "library_checkout",
    'application':True,
    'sequence':-99,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    

    # any module necessary for this one to work correctly
    'depends': ['library_member','mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        
        "views/library_checkout_menu.xml",
        "views/wizard_view.xml"
    ],
    # only loaded in demonstration mode
    
}
