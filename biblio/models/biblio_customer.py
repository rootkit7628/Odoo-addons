from odoo import models, fields


class Customer(models.Model):
    """
        A Model for the customers of the biblio of Brussels
    """
    
    _name = "biblio.customer"
    _description = "Library Customer"

    name = fields.Many2one("res.partner", string="Full name")
    email = fields.Char("Email")
    adress = fields.Char("Adress")
    telephone =  fields.Integer("Tel")
    book_rents = fields.Many2many("biblio.book", string="Books renteds")
    