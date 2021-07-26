from odoo import fields, models


class Expertise(models.Model):
    """
        A class that implement the type of expertise avalaible
        in the Citadels
    """

    _name = "citadel.maester.expertise"
    _description = "Different expertise avalaible in the citadels"
    name = fields.Char("Name")
