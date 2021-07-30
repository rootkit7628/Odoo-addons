from odoo import models, fields


class Rental(models.Model):
    """
        The history of the book rented by customers on the library
    """

    _name = 'biblio.rental'
    _description = 'Library Rentals'

    book_id = fields.Many2one("biblio.book")
    customer_id = fields.Many2one("biblio.customer")

    rental_date = fields.Date(string="Rental date")
    turnin_date = fields.Date(string="Turn in date")

    customer_email = fields.Char(related='customer_id.email')
    customer_tel = fields.Integer(related='customer_id.telephone')
    customer_adress = fields.Char(related='customer_id.adress')

    book_authors = fields.Many2many(related="book_id.author_ids")
    book_isbn = fields.Char(related="book_id.isbn")
