{
     'name':'rootkit',
     'version':'1.0',
     'summary':'A module test',
     'description':'Just a module to do some test',
     'author':'Arleme J.',
     'depends':['base'],
     'application': True,
     'installable': True,
     'data':[
          'security/security_file.xml',
          'security/ir.model.access.csv',
          'views/rootkit_menu.xml',
          'views/rootkit_list.xml',
          'views/book_list_template.xml',
     ]
}
