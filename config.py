


rules = {
    'archive': True,
    'send_mail': True,

    #'preferred': None,
    'preferred': ['BTC', 'IRR', 'IQD', 'USD', 'AED'],
    'notification': {
        'enable': True,
        'number': '09111127685',
        'preferred': {
            'BTC': {'min': 0.000101, 'max': 0.000104},
            'IRR': {'min': 45000, 'max': 50000}
        }
    }
}

