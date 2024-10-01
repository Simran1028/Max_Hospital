{
    'name' : 'Hospital Management',
    'author' : 'Sutraa Technosoft',
    'license' : 'LGPL-3',
    'version' : '17.0.1.0',
    'sequence' : -100,
    'depends' :[
        'mail', 'product',
        ],
    'data' : [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/female_patient_view.xml',
        'views/male_patient_view.xml',
        'views/appointment.xml',
        'views/patient_tag.xml',
        'reports/patient_card.xml',
        'reports/patient_details_template.xml',
        'reports/reports.xml',
       
              ],
    'installable': True,
    'application': True,
}