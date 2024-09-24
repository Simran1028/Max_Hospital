# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Motorcycle Registry',
    'version': '17.0.1.0',
    'summary': 'Registry of Motorcycles',
    'depends': ['base'],
    'category': 'Inventory/Inventory',
    'demo': [
        
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/motorcycle_registry_security.xml',
        'views/motorcycle_registry_view.xml',
       
    ],
    'demo':[
        'demo/demo_data.xml',
    ],
    'installable': True,
    'application': True,
    
    'license': 'LGPL-3',
}
