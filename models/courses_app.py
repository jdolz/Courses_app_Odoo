# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Courses_course(models.Model):
    _name = 'courses.course'
    _description = 'Courses'

    name = fields.Char('Title', required=True)
    professor = fields.Char('Professor', required=True)
    price = fields.Float('Price', required=True)
    date_ini = fields.Date('Start Date', required=True)
    number_employees = fields.Integer('Number of Registered Employees')
    duration = fields.Char('Duration', required=True)
    certificate = fields.Boolean('Offers Certificate')
    contents = fields.Text('Contents')
    total = fields.Float('Total Price', compute="_total", store=True)
    

    @api.depends('price','number_employees')
    def _total(self):
        for r in self:
            r.total = r.number_employees*r.price

    
