from odoo import models, fields

""" Se recomienda hacer primero estos modelos que no dependen de otros """


class BibliotecaGenero(models.Model):
    _name = 'bibliotecasge.genero'
    _description = 'Géneros literarios'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')

    # Relación Many2many: un género puede estar en muchos libros
    # y un libro puede tener muchos géneros
    libro_ids = fields.Many2many(
        'bibliotecasge.libro',        # Modelo relacionado
        string='Libros con este género'
    )