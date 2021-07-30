{
    'name':'The Citadel OpenAcademy',
    'summary':'Manage the training of the future maesters of the citadels',
    'description':'''In this system, the citadel manage the
         training sessions of its future maesters.''',
    'author':'Arleme J.',
    'depends':[
        'base',
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/citadel_menu.xml',
        'views/citadel_maester.xml',
        'views/course_list.xml',
        'views/session_list.xml',
    ],
    'application': True,
    'installable': True
}
