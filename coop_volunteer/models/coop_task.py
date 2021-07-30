from odoo import models,fields


class Task(models.Model):
    """
        Task Model
    """
    _name =  "coop.task"
    _description = "Cooperative Tasks"

    name = fields.Char(Required=True)

    task_type = fields.Selection(
        (
            ("r","Recurring tasks"),
            ("o","One-shot tasks")
        ),
        "Task Type"
    )
    
    begin_time = fields.Datetime()
    duration = fields.Float(string="Duration")

    volunters_ids = fields.Many2many("coop.volunteer",string="Volunteers participating")
    volunteer_nb = fields.Integer(string="Number of volunteers needed")

    active = fields.Boolean("Active  ?", default=True)
