from odoo import api, fields, models, tools, _

class Enquiry(models.Model):
    _inherit = 'purchase.order'

    x_many2many = fields.Many2many('purchase.order.line',domain="[('partner_id', '=', '线下采购')]",string=u'多选')

#     @api.constrains('x_many2many')
#     def _get_order(self):
#         for i in self.x_many2many:
#             if i:
#                 self.write({'order_line':self.x_many2many,'x_many2many':None})
