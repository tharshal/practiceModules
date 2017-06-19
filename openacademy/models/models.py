# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Course Name", required=True)
    description = fields.Text()
    courseDuration = fields.Text()
    about = fields.Text()

    responsible_id = fields.Many2one('res.users',ondelete='set null', string="Responsible", index=True)
    session_ids = fields.One2many(
        'openacademy.session', 'course_id',string="Sessions")


    '''@api.multi
    def _compute_name(self):
        for record in self:
            record.name = str(random.randint(1,1e6))
'''

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
###Domain------------------->>>>>>>>>>>>>>>>
###------------------------------------------------------>>>>>

    instructor_id = fields.Many2one('res.partner', string="Instructor",domain=['|',('instructor','=',True),
                                                                                ('category_id.name','ilike',"Teacher")])
    course_id = fields.Many2one('openacademy.course',ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

    university = fields.Char(string="University",compute="_compute_name",store=True)
    value = fields.Integer(string="value")

###depends------------------
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        import pdb
        #pdb.set_trace()
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.depends('value')
    def _compute_name(self):
        for record in self:
            record.university = record.university + record.value + 130




###onchage-------------------
    @api.onchange('seats','attendee_ids')
    def _verifySeats(self):
        if self.seats < 0:
            return{
            'warning':{
                    'title':"Incorrect Seats value...",
                    'message' : "The seat number may not be negative",
                },
            }
        if self.seats < len(self.attendee_ids):
            return{
            'warning':{
                    'title':"Too many Attendees",
                    'message' : "Increase seats or remove excess attendees",
                    }
            }

    @api.constrains('instructor_id','attendee_ids')
    def _chk_instructor_not_attendee(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise exceptions.ValidationError("A sessions Instructor can't be Attendee")
