# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Reparaciones(models.Model):
    _inherit = 'repair.order'

    so_id = fields.Many2one(comodel_name='sale.order', string='Nota de Venta')

    
    
