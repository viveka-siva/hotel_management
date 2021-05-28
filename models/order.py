from odoo import models, fields, api

class RestuarantOrder(models.Model):
    _name = 'order.item'
    dish = fields.Char(string='Dish')
    quantity = fields.Integer(string='Quantity')
    price = fields.Float(string='Price')
    total = fields.Integer(string='Total')
    waiter_id = fields.Many2one('hotel.person', string='Waiter',
                                domain=[('person type','=','waiter')])
    state = fields.Selection([('new', 'New'),
                              ('kitchen', 'Kitchen'),
                              ('in_process', 'In Process'),
                              ('ready', 'Ready'),
                              ('delivered', 'Delivered'),
                              ('bill', 'Bill'),
                              ])
    def create(self,vals):
        print('vals',vals)
        print('self',self)
        qty=vals.get('quantity',0)
        price=vals.get('price,',0)
        vals.update({'total':qty*price})
        return super(RestuarantOrder, self).create(vals)

    def write(self,vals):
        print('self',self)
        #self is a recordset
        print('vals',vals)
        if vals.get('quantity',False) or vals.get('price'):
            print('enter if statement')
            qty=vals.get('quantity',False)
            print('quantity',0)
            print('quantity',qty)
            price=vals.get('price',0)
            print('price',price)
            if not qty:
                print('in if not qty')
                qty=self.quantity
            if not price:
                print('in if not price')
                #get price from record
                price=self.price
                print('quantity',qty)
                print('price',price)
                vals.udate({'total':qty*price})
        print(vals)
        return super(RestuarantOrder, self).write(vals)

    def set_new(self):
        vals={'state':'new'}
        self.write(vals)
        return True
    def duplicate_order(self):
        vals={'dish':self.dish,
              'price':self.price,
              'quantity':self.quantity,
              'total':self.total,
              'waiter_id':self.total,
              'state':self.state}
        res = self.create(vals)
        return res






