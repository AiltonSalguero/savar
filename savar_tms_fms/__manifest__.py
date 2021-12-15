{
    'name': """
	Savar TMS Field Service
    """,

    'summary': """
    """,

    'description': """
    """,

    'category': 'Warehouse',
    'version': '14.0',

    'depends': [
        'stock',
    ],

    'data': [
        'views/project_task_views.xml',
        'security/ir.model.access.csv',
    ],
    
    'images': ['static/description/banner.png'],
    
    'application': True,
    'installable': True,
    'auto_install': False,
}
