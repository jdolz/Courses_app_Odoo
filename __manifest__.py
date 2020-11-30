{
    'name': 'Courses Application',
    'version': '1.0',
    'description': 'Manage the courses for your employees.',
    'author': 'EEP - Javier Dolz',
    'depends': ['base'],
    'application': True,
    'data': [
        'views/courses_app_views.xml',
        'security/ir.model.access.csv',
        'security/courses_access_rules.xml',
    ],
}
