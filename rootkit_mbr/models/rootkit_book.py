from odoo import fields, models


class Book(models.Model):
    """
        Class Book for showig if a book is available for a user
    """
    _inherit = 'rootkit.book'
    is_available = fields.Boolean('Is Available?')

    isbn = fields.Char(help="Use a valid ISBN-13 or ISBN-10.")
    publisher_id = fields.Many2one(index=True)
    