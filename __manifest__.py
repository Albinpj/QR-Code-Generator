{
    'name': 'QR Generator',
    'version': '15.0.1.0',
    'sequence': -3002,
    'category': 'QR For The Text',
    'summary': 'QR For The Text',
    'application': True,
    'depends': [
        'base',
        'sale_management',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/qr_generator_syntray.xml',

    ],
    'assets': {
       'web.assets_backend': {
           '/qr_generator/static/src/js/qr_icon.js',
       },
       'web.assets_qweb': {
           '/qr_generator/static/src/xml/qr_icon.xml',
       },
    },

}
