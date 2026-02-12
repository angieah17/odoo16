{
    'name': 'Biblioteca Escolar',
    'version': '16.0.0.1.0',
    'summary': 'Gestiona los libros de nuestra biblioteca escolar',
    'description': 'Gestión sencilla de los libros escolares (recursos de las asignaturas).',
    'author': 'Mi nombre',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/libro_views.xml',
    ],
    'installable': True,
    'application': True,
}

