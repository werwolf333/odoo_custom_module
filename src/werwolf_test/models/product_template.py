# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import timedelta, time
from odoo import api, fields, models
from odoo.tools.float_utils import float_round


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = "product.template"
    manufacturer_id = fields.Many2one('product.manufacturer', string='Manufacturer')
    model_id = fields.Many2one('product.model', string='Model')


class ProductManufacturer(models.Model): 
    _name = 'product.manufacturer'
    name = fields.Char(string='Name', required=True)
    model_id = fields.One2many('product.model', 'manufacturer_id')
    product_template_id = fields.One2many('product.template', 'manufacturer_id', string="Product")


class ProductModel(models.Model):
    _name = 'product.model'
    name = fields.Char(string='Name', required=True)
    manufacturer_id = fields.Many2one('product.manufacturer', string='Manufacturer')
    product_template_id = fields.One2many('product.template', "model_id", string="Product")

