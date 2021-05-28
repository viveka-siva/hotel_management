# -- coding: utf-8 --
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'hotel_management',
    'version': '0.1',
    'summary': 'Simple hotel management functions',
    'description': """This module is for training purpose on hotel mangement
    """,
    'depends': ['base'],
    'data': [
        'views/hotel.xml',
        'views/food.xml',
        'views/order.xml',
        'views/kitchen.xml',
    ],
    'installable': True,
    'auto_install': False
}