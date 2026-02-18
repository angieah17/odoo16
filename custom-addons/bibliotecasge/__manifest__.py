{
    'name': 'Biblioteca SGE',
    'version': '16.0.0.2.0',  # Versión actualizada
    'summary': 'Gestión de biblioteca con autores y géneros',
    'description': '''
        Módulo de biblioteca con:
        - Gestión de libros
        - Catálogo de autores
        - Clasificación por géneros
    ''',
    'author': 'Angie Amado',
    'depends': ['base'],
    'data': [
        # Seguridad primero
        'security/ir.model.access.csv',

        # Vistas (el orden importa: primero libro porque define el menú raíz)
        'views/libro_views.xml',
        'views/autor_views.xml',
        'views/genero_views.xml',
    ],
    'installable': True,
    'application': True,
}