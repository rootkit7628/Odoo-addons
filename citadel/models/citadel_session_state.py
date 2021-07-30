from odoo import models, fields


class SessionState(models.Model):
    """
        Model of the state of the session of the citadel
        """
    _name = "citadel.session.state"
    _description = "Session state"

    name = fields.Char("Name")
    active = fields.Boolean("Active ?",default=True)
    order = fields.Integer("Order",default=1)
