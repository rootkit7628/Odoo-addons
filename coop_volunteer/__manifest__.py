# -*- coding: utf-8 -*-
{
     'name':'Cooperative Volunteers',
     'version':'1.0',
     'summary':'Organize the work of volunteers',
     'description':'A module to organize the work of the volunteers of the cooperative.s',
     'author':'Arleme J.',
     'depends':['base'],
     'application': True,
     'installable': True,
     'data':[
          'security/ir.model.access.csv',
          'views/coop_menu.xml',
          'views/task_view.xml',
          'views/volunteer_view.xml',
     ],
     'css':[
          'static/src/css/task.css',
     ],
     'demo':[
        'data/coop.volunteer.csv',
    ],
}
