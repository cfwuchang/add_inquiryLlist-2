from odoo import api, fields, models

class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    x_many2many_list = fields.Many2many('purchase.order.line',domain="[('partner_id', '=', '线下采购')]",string=u'多选')
    x_vendor_id = fields.Many2one('res.partner', string="供应商",related ='purchase_ids.partner_id')

    @api.constrains('x_many2many_list')
    def get_requisition(self):
        all_data = []
        for i in self.x_many2many_list:
            dones = self.env['purchase.order.line'].sudo().browse(int(i.id))
            all_data.append((0,False, {'product_id': i.product_id.id,'product_qty':i.product_qty,'qty_ordered':i.qty_received,
            'product_uom_category_id':i.product_uom_category_id.id,'product_uom_id':i.product_uom.id,
            'account_analytic_id':i.account_analytic_id.id,'analytic_tag_ids':i.analytic_tag_ids.id,'price_unit':i.price_unit}))
            dones.unlink()
        if all_data:
            self.write({'line_ids': all_data})
            self.write({'x_many2many_list': None})