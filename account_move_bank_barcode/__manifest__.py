# -*- coding: utf-8 -*-
{
    'name': "account_move_bank_barcode",

    'summary': """
        Agrega codigo de barras al reporte de factura de odoo""",

    'description': """
        Agrega codigo de barras al reporte de factura de odoo:
        - codigo de barra = nro_convenio (char 1 - 3 obligatorio)
        nro_factura_cbte (char 4 - 15 obligatorio)
        fecha_vto (char 16 - 21 obligatorio)
        importe (char 22 - 33 obligatorio)
        espacio_libre (char 34 - 50)
        
        Fuente Cod128 estandar
    """,

    'author': "Devoogroup",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account',
                'sale'],

    # always loaded
    'data': [
        'views/account_move_views.xml',
        'views/report_invoice.xml',
    ],
}
