from odoo import models, fields, api, _

class HrInsurance(models.Model):
    _name = 'hr.insurance.policy'
    _description = "Insurance Policy"
    _rec_name = "partner_id"
    partner_id = fields.Many2one('res.partner', string='Partner name', domain=[('insurance', '=', True)])
    start_date = fields.Date('Start date')
    end_date = fields.Date('End date')
    ref_num = fields.Integer(string='Reference No:', translate=True)
    vendor_num = fields.Integer(string='Vendor Bill No:', required=1)
    insurance_status = fields.Boolean(string='Status')
    class_id = fields.Many2many('hr.class.network', string='Classes') 

class HrInsuranceClass(models.Model):
    _name = 'hr.insurance.class'
    _description = "Insurance Class"
    name = fields.Char('Name', required=1, translate=True)
    status = fields.Boolean(string='Status', required=1, translate=True)


class HrInsuranceClassNetwork(models.Model):
    _name = 'hr.class.network'
    _description = "Insurance Class Network"
    _rec_name = "network"
    network = fields.Char('Network', required=1, translate=True)
    policy_no = fields.Many2one('hr.insurance.class', string='Class')  

class HrDependent(models.Model):
    _name = 'hr.dependent'
    _description = 'insurance dependant'

    name = fields.Char(string='Name')
    relation = fields.Selection([(('parent', 'Parent'),
                                     ('spouse', ' Spouse'),
                                     ('child', 'Child'))], string='Relation')
    birth_date = fields.Date('Birth Date')
    policy_no = fields.Many2one('hr.insurance.policy', string='Insurance Policy No.:')
    class_id = fields.Many2one('hr.insurance.class', string='Class ')
    insurance_member_id = fields.Integer(string='Insurance Member No:')
    iqama_id = fields.Integer(string='Iqama ID:')
    iqama_date = fields.Date('Iqama Expiry date')
    passport_id = fields.Integer(string='Passport No:')
    passport_date = fields.Date('Passport Expiry date')

