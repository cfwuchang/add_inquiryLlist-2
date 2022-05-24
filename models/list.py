from odoo import api, fields, models, tools, _

class List(models.Model):
    _inherit = 'purchase.order.line'

    x_price= fields.Float(string=u'含税单价',compute='_get_x_price',readonly=False,store=True,
    inverse='_set_x_price')

    @api.depends('price_unit','taxes_id')
    def _get_x_price(self):
        for i in self:
            if not (i.price_unit and i.taxes_id):
                i.x_price=i.price_unit
                continue
            aa=i.x_price
            bb=i.taxes_id.amount
            aa=((bb+100)/100)*aa
            i.x_price=aa

    def _set_x_price(self):
         for i in self:
            if not (i.x_price and i.taxes_id):
                continue
            aa=i.x_price
            bb=i.taxes_id.amount
            aa=aa/((bb+100)/100)
            i.price_unit=aa