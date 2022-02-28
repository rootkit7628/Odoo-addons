# -*- coding: utf-8 -*-
{
    'name': 'CS Invoice',
    'summary': 'Custom Invoice Addons',
    'description': """
        Just to generate custom invoice report
    """,
    'author': 'Arleme Johnson',
    'version': '1.0',
    'depends': ['base',
                'contacts'
                ],

    'data': [
        # data

        # security

        # views

        # reports
        'report/cs_invoice_report.xml',

        # wizards

    ],
    'demo': [
    ],
    'installable': True,
    'application': False
}