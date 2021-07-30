from odoo import fields, models


class Course(models.Model):
    """
        A class that implement the type of course avalaible
        in the Citadels
    """

    _name = "citadel.course"
    _description = "Differents courses avalaible in the citadels"
    name = fields.Char("Name")
    active = fields.Boolean(default=True)
    volunteer_id = fields.Many2one("res.users", string="Professors")
    level = fields.Selection(
        (
            ("n","Novice"),
            ("m","Normal"),
            ("a","Skilled"),
            ("g","Expert")
        ),
        "Level"
    )
