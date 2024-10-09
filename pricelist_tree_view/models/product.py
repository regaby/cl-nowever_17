   ##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################
from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit ='product.template'
    _name = 'product.template'

    listprice_price = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta"
    )
    listprice_price2 = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta 2"
    )

    def _compute_price(self):
        listprice_tree_view = self.env.user.company_id.tree_view_pricelist_id.id
        listprice_tree_view2 = self.env.user.company_id.tree_view_pricelist2_id.id
        for rec in self:
            if rec:
                price = rec.with_context(pricelist=listprice_tree_view)._get_contextual_price()
                rec.listprice_price = price
                try:
                    prod = self.env['product.product'].search([('product_tmpl_id','=',rec.id)])
                    price2 = prod.with_context(pricelist=listprice_tree_view2)._get_contextual_price()
                    rec.listprice_price2 = price2
                except:
                    rec.listprice_price2 = False

class ProductProduct(models.Model):
    _inherit ='product.product'

    listprice_price = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta"
    )
    listprice_price2 = fields.Float(
        compute='_compute_price',
        help='Price for product specified on the context',
        string="Precio de venta 2"
    )

    def _compute_price(self):
        listprice_tree_view = self.env.user.company_id.tree_view_pricelist_id.id
        listprice_tree_view2 = self.env.user.company_id.tree_view_pricelist2_id.id
        for rec in self:
            if rec:
                price = rec.with_context(pricelist=listprice_tree_view)._get_contextual_price()
                rec.listprice_price = price
                try:
                    price2 = rec.with_context(pricelist=listprice_tree_view2)._get_contextual_price()
                    rec.listprice_price2 = price2
                except:
                    rec.listprice_price2 = False


