from odoo import models, fields, api


class Kitchen(models.Model):
    _name = 'kitchen.product'
    name = fields.Char(string='Name')
    expiry = fields.Integer(string='Expiry')
    weight = fields.Float(string='Weight')
    count = fields.Integer(string='Count')
    is_refrigerated = fields.Boolean(string="Active", required=True)


