from odoo import fields, models


class Book(models.Model):
    """
        Model for the books of the library
    """
    _name = 'biblio.book'
    _description = 'Library book'

    name = fields.Char("Name")
    author_ids = fields.Many2many("res.partner",string="Author")
    isbn = fields.Char("ISBN Number")
    editor = fields.Char("Editor")
    year_edition = fields.Selection(
        tuple(('x1',x) for x in range(1800,2030)),
        'Year of edition'
    )

    rental_ids = fields.One2many('biblio.rental', 'book_id', string='Rental of book')
