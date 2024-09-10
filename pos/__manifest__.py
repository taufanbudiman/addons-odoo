# -*- coding: utf-8 -*-
{
    'name': "Point of Sales (Customize)",

    'summary': """
        Beberapa custom modul untuk POS
    """,

    'description': """
        Beberapa custom modul untuk POS
    """,

    'author': "Tim Odoo",
    'website': "https://www.odoo.com/",
    'category': 'Sales/Point of Sale',
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['web', 'point_of_sale'],
    'data': [
        'views/pos_asset_customization.xml',
    ],
    'license': 'AGPL-3'
}