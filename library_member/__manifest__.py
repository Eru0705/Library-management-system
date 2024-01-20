# -*- coding: utf-8 -*-
{
    'name': "library_member",
    "sequence": -99,
    'application': True,

    'description': """
        Manage books
    """,
    'category': 'uncategorized',
    'version': '0.1',
    
    
    'depends': ['library_app'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/library_menu.xml'
    ],
    
}
