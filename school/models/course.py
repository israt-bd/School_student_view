from odoo import models , fields, api , _

class Course(models.Model):
    _name = 'school.course'
    _description = 'course'
    name = fields.Char('course Name', required=True)
    code = fields.Char('Code')
