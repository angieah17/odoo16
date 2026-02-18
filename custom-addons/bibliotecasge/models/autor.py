from odoo import models, fields

""" Se recomienda hacer primero estos modelos que no dependen de otros """

class BibliotecaAutor(models.Model):
    _name = 'bibliotecasge.autor'
    _description = 'Autores de los libros'

    name = fields.Char(string='Nombre', required=True)
    nacionalidad = fields.Char(string='Nacionalidad')
    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')

    # Relación One2many: un autor tiene muchos libros
    # Parámetros: modelo relacionado, campo Many2one en ese modelo
    libro_ids = fields.One2many(
        'bibliotecasge.libro',  # Modelo destino
        'autor_id',                  # Campo Many2one en Libro
        string='Libros escritos'
    )