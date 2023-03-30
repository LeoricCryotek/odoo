
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models

class estateProperty(models.Model):
    _name = "estate.model"
    _description = "Estate plans"

    #id (Id)
    #create_uid
    #create_date (Datetime)
    #write_uid
    #write_date
    name = fields.Char('Property Name', required=True, translate=True)
    description = fields.Char()
    postcode = fields.Char('Postal Code')
    #date_availability
    #expected_price
    #selling_price
    #bedrooms
    #living_area
    #facades
    #garage
    #garden
    #garden_area
    garden_orientation = fields.Char()

