# -*- coding: utf-8 -*-
{
    'name': "bets",

    'summary': """
        Módulo para gestionar empresa de apuestas deportivas""",

    'description': """
        Este módulo ofrece una gestión completa para tu empresa de apuestas deportivas, te permite tanto
        gestionar los empleados con su puesto como los clientes con sus saldos, además de realizar apuestas
        a eventos deportivos por cada cliente.
    """,

    'author': "Iñigo Madrigal",
    'website': "http://www.betcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'betcompany',
    'version': '1.9',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
