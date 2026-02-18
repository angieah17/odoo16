from odoo import models, fields

class BibliotecaLibro(models.Model):
    _name = 'bibliotecasge.libro'
    _description = 'Libros de la biblioteca'

    name = fields.Char(string='Título', required=True)
    isbn = fields.Char(string='ISBN')
    state = fields.Selection([
        ('available', 'Disponible'),
        ('borrowed', 'Prestado')
    ], default='available', string='Estado')

    # ============================================
    # NUEVAS RELACIONES
    # ============================================

    # Many2one: muchos libros → un autor
    # NOTA: Sin required=True para poder crear libros sin autor asignado
    autor_id = fields.Many2one(
        'bibliotecasge.autor',
        string='Autor',
        ondelete='set null'  # Si se borra el autor, el libro queda sin autor
    )

    # Many2many: un libro puede tener varios géneros
    genero_ids = fields.Many2many(
        'bibliotecasge.genero',
        string='Géneros'
    )