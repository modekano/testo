from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    insur_policy = fields.Many2one('hr.insurance.policy',string="Insurance Policy No.:")
    insur_class = fields.Many2one('hr.insurance.class',string="Class:")
    insur_member = fields.Integer(string="Insurance Member No.:")
    insur_dependent = fields.Many2one('hr.dependent',string="Dependent")
