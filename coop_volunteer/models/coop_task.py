# -*- coding: utf-8 -*-
from datetime import datetime
from pytz  import UTC
from odoo import models, fields, api


def format_float_time(flt):
    '''
        Format a time in float to format "%H:%m "
    '''
    return f"{str(int(flt)).zfill(2)}:{ str(int(round( (flt - int(flt)) * 60 , 0))).zfill(2) }"


def float_to_hour_min(flt):
    '''
        Get the minute and the hour from a time on float
        return a tuple (hour, min)
    '''
    return ((int(flt)), int(round( (flt - int(flt)) * 60 , 0)))


class Task(models.Model):
    '''
        Task Model
    '''
    _name =  "coop.task"
    _description = "Cooperative Tasks"

    name = fields.Char(Required=True)

    task_template_id = fields.Many2one("coop.task.template", string="Task Template")
    task_type_id = fields.Many2one("coop.task.type" ,string="Task Type")

    begin_time = fields.Datetime()
    finish_time = fields.Datetime()

    volunteer_id = fields.Many2one("coop.volunteer",string="Assignement")

    active = fields.Boolean("Active  ?", default=True)


class TaskType(models.Model):
    '''
        Task Type
    '''
    _name = "coop.task.type"
    _description= "Cooperative Task Type"

    name = fields.Char()
    description = fields.Char()

    area = fields.Char()
    active = fields.Boolean(default=True)


class TaskTemplate(models.Model):
    '''
        Task Template
    '''
    _name = "coop.task.template"
    _description = "Cooperative Task Template"

    name = fields.Char(required=True)

    task_type_id = fields.Many2one('coop.task.type', string='Task Type')

    str_time = fields.Float()
    end_time = fields.Float()

    task_area = fields.Char(related='task_type_id.area', string='Task Area')

    duration = fields.Float(compute="_compute_duration", string="Duration")

    volunteer_nb = fields.Integer(string="Number of volunteers", default=1)
    volunteer_ids = fields.Many2many("coop.volunteer",string="Predefined Worker")

    active = fields.Boolean("Active ?")

    floating = fields.Boolean(string="Floating Task ?")

    @api.depends('str_time', 'end_time')
    def _compute_duration(self):
        for template in self:
            template.duration =  template.end_time - template.str_time

    @api.onchange('floating')
    def _onchange_floating(self):
        if self.floating:
            self.volunteer_ids = self.env["coop.volunteer"]

    @api.multi
    def generate_task(self):
        '''
            Methode toGenerate a new task
        '''
        self.ensure_one()
        task = self.env['coop.task']

        h_begin, m_begin = float_to_hour_min(self.str_time)
        h_end, m_end = float_to_hour_min(self.end_time)
        for i in range(0, self.volunteer_nb):
            task.create({
                'name': f"[{i}] {self.name} | {self.str_time} - {self.end_time}",
                'task_template_id': self.id,
                'task_type_id': self.task_type_id.id,
                'volunteer_id': self.volunteer_ids[i].id if len(self.volunteer_ids) > i else False,
                'begin_time': fields.Datetime.context_timestamp(self, datetime.today()).replace(hour=h_begin, minute=m_begin, second=0).astimezone(UTC),
                'finish_time': fields.Datetime.context_timestamp(self, datetime.today()).replace(hour=h_end, minute=m_end, second=0).astimezone(UTC)
            })