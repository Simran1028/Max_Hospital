{
    'name' : 'Hospital Management',
    'author' : 'Sutraa Technosoft',
    'license' : 'LGPL-3',
    'version' : '17.0.1.0',
    'sequence' : -100,
    'depends' :[
        'base_setup','base','digest','mail'
        ],
    'data' : [
        'views/menu.xml',
        'views/female_patient_view.xml',
        'views/male_patient_view.xml',
        'views/appointment.xml',
        'max_hospital/security/ir.model.access.csv',
              ],
    'installable': True,
    'application': True,
}