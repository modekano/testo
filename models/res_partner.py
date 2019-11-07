from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    insurance = fields.Boolean(string="Authorized party for medical insurance")
