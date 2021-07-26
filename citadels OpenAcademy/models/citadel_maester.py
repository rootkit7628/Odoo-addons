from odoo import models, fields


class Maester(models.Model):
    """
        Model for existing the order of intellectuals
        (scholars, healers, and other learned men) in citadels of the Seven Kingdoms.
    """

    _name = "citadel.maester"
    _description = "A maester of the citadel of the seven kingdom"
    name = fields.Char("Name", required=True)
    entering_date = fields.Date()
    photo = fields.Binary("Cover")
    role = fields.Selection(
        (
            ("n","Noobs"),
            ("m","Maester"),
            ("a","ArchiMaester"),
            ("g","GrandMaester")
        ),
        "Level"
    )
    status = fields.Boolean("Alive ?", default=True)
    expertise_id = fields.Many2one('citadel.maester.expertise', string='Expertise', required=True)
