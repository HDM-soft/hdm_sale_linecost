# -*- coding: utf-8 -*-
{
    "name": "hdm_sale_linecost",
    "summary": """
        This module extends the sales order line, adding a field with the cost price of each product per quantity.""",
    "description": """
        Sale Line Cost
    """,
    "author": "Horacio Montaño",
    "company": "HDMSOFT",
    "website": "https://odoo.hdmsoft.com.ar",
    "license": 'AGPL-3',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Sales",
    "version": "16.0.0.0.0",
    # any module necessary for this one to work correctly
    "depends": ["sale", "product"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/sale_order_linecost_view.xml",
    ],

    "instalable": True,
    'application': False,
    'auto_install': False,
}
