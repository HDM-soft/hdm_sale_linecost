# -*- coding: utf-8 -*-
# models/sale_order_line.py
from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    cost_total = fields.Monetary(
        string='Total Cost',
        compute='_compute_cost_total',
        store=True,
        currency_field='currency_id'
    )

    currency_id = fields.Many2one(
        related='order_id.currency_id',
        store=True,
        string='Currency',
        readonly=True
    )

    @api.depends('product_id', 'product_uom_qty')
    def _compute_cost_total(self):
        for line in self:
            product_cost = line.product_id.standard_price
            line.cost_total = product_cost * line.product_uom_qty
