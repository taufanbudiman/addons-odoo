# -*- coding: utf-8 -*-
{
    'name': "Material",

    'summary': """
        Modul Material
    """,

    'description': """
        Modul Material
    """,

    'author': "Tim Odoo",
    'website': "https://www.odoo.com/",
    'category': 'Administration/Materials',
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/material_views.xml',
    ],
    'assets': {},
    'license': 'AGPL-3'
}