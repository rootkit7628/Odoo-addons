from odoo import models, fields


class Maester(models.Model):
    """
        Model for existing the order of intellectuals
        (scholars, healers, and other learned men) in citadels of the Seven Kingdoms.
    """
    
    _inherit = "res.partner"
    _name = "res.partner.maester"
    professor = fields.Boolean(default=False)
