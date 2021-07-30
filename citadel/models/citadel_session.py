from odoo import api, models, fields
from odoo.exceptions import Warning

class Session(models.Model):
    """
        The session of courses attendees by thoses maesters
    """

    _name = "citadel.session"
    _description = "Session of course"

    volunteer_id = fields.Many2one('citadel.maester', string='Professor', required=True)

    date_begin = fields.Datetime()
    date_finish = fields.Datetime()

    room = fields.Selection(
        tuple(('n'+str(i),'Room'+str(i)) for i in range(1,10))
            +
        (('l', 'laboratory'),('s', 'stade'))
        ,'Room'
    )

    course_id = fields.Many2one('citadel.course', string='Course', required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendes')
    professor_id = fields.Many2one('res.partner', string="Instructor")
    state = fields.Many2one('citadel.session.state', string="State", Required=True)

    place_nb = fields.Integer(string="Number of Places")

    place_occuped = fields.Integer(compute='_compute_place_occuped', store=False, string="Place occuped (%)")

    @api.depends('place_nb', 'attendee_ids')
    def _compute_place_occuped(self):
        for session in self:
            if not session.place_nb:
                session.place_occuped = 0
            else:
                session.place_occuped = 100 * len(session.attendee_ids) / session.place_nb
            if session.place_occuped > 100:
                raise Warning("You can't have more than %s attendees for this session." % session.place_nb)
   
    @api.constrains('place_nb','attendee_ids')
    def _check_attendee_ids(self):
        for session in self:
            if session.place_occuped > 100:
                raise Warning(
                    "You can't have more than %s attendees for this session." % session.place_nb
                )
