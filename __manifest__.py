{

    'name': 'HR Medical Insurance ',
    'version': '12.0',
    'author': 'Bankruptcy committee',
    'depends': ['hr_base','hr'],
    'data': [
        'security/ir.model.access.csv',
        # 'data/hr_experience_data.xml',res_config_settings
        'view/hr_medical_insurance.xml',
        'view/contact.xml',
        'view/res_config_settings.xml'
        ],
    'installable': True,
}
