from odoo import models, fields, api


class Person(models.Model):
    _name = 'hotel.person'
    name = fields.Char(string='Person ')
    age = fields.Integer(string='Age')
    weight = fields.Float(string='Weight')
    dob = fields.Date(string='Date of birth')
    marital_status = fields.Boolean(string='Marital Status')
    joining_date = fields.Datetime()
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female'),
                               ('transgender', 'Transgender'),
                               ])
    orders = fields.One2many('order.item', 'waiter_id', string='Orders')
    # Waiter_id1 = fields.One2many('restuarant.order', 'Waiter_id1)
    # waiter_id = fields.many2one('hotel.person', 'Waiter')
    person_type = fields.Selection([('waiter', 'Waiter'),
                                    ('customer', 'Customer'),
                                    ('chef', 'Chef'),
                                    ], default='waiter')
