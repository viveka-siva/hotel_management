from odoo import models, fields, api


class FoodMenu(models.Model):
    _name = 'food.menu'
    name = fields.Char(string='Dish_Name')
    price = fields.Float(string='Price')
    # orders_items = fields.Many2one('order.item',string='Order List')