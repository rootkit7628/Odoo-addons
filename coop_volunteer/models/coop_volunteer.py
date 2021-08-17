# -*- coding: utf-8 -*-
from odoo import fields, models


class Volunteers(models.Model):
    """
        Model for volunteers of the cooperative
    """
    _name = "coop.volunteer"
    _description = "Cooperative volunteers"

    name = fields.Char("Full name",Required=True)
    adress = fields.Char("Adress")
    tel =  fields.Integer("Tel")

    photo = fields.Binary("Photo")
