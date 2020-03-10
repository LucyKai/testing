# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class custom_module(models.Model):
    # _inherit = 'product.template'
   
    _name = 'custom.pos'

    name = fields.Char()
    feedback = fields.Text(string = "Feedback")
    check = fields.Boolean(string="check",default=True)
    editview = fields.Html(string="Comment")
    age = fields.Integer(string="Age")
    salary = fields.Float(string="Salary")
    datetime = fields.Datetime(string="Record Date Time",default=fields.Datetime.now,required=True)
    date = fields.Date(string="Record Date",required=True)
    image = fields.Binary(string="Image")
    hobby = fields.Selection([ ('type1', 'Reading'),('type2', 'Swimming'),('type3', 'Sleeping'),],'Hobby')
    aref = fields.Reference([('pos.category','POS Category')])
    pos = fields.Many2one('pos.category', string='Parent Category')
