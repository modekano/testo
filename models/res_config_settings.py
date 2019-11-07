# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class ResCompany(models.Model):
#     _inherit='res.company'

#     add_insurance = fields.Boolean('Allow Saudi Employees to add insurance for their parents')
#     insurance_max_num = fields.Integer('Maximum Number of Included Childs for each Employee', default=0)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    add_insurance = fields.Boolean('Allow Saudi Employees to add insurance for their parents', readonly=False,
                                            #   company_dependent=True, related='company_id.add_insurance'
                                              )
    insurance_max_num = fields.Integer('Maximum Number of Included Childs for each Employee', default=0)


    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            add_insurance=(params.get_param('hr_medical_insurance.add_insurance', default=True)),
            insurance_max_num=(params.get_param('hr_medical_insurance.insurance_max_num', default=True))
        )
        return res

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('hr_medical_insurance.add_insurance',
                                                         self.add_insurance)
        self.env['ir.config_parameter'].sudo().set_param('hr_medical_insurance.insurance_max_num',
                                                         self.insurance_max_num)
                                                    

