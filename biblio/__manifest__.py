{
    'name' : 'Library Management',
    'summary' : 'Manage their books and customers',
    'description' : '''A module for managing Brussels library
     with their books and theuir customers''',
    'version' : '1.0',
    'depends':[
        'base'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/biblio_menu.xml',
    ],
    'application': True,
    'installable': True
}
