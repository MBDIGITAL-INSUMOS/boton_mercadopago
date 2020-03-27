{
    'name': 'Button for MercadoPago',
    'category': 'Account',
    'version': '0.1',
    'depends': ['account','base'],
    'data': [
	'invoice_view.xml',
	'invoice_action_data.xml'
    ],
    'external_dependencies':{
            'python': ['mercadopago'],
        },
    'demo': [
    ],
    'qweb': [],
    'installable': True,
}
