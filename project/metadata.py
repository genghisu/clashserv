import os

try:
    from __revision__ import __revision__
except:
    __revision__ = 'develop'

metadata = {
    'name': "clashserv",
    'version': "1.0",
    'release': __revision__,
    'url': 'http://lottserv.hanboxllc.com',
    'author': 'hanbox',
    'author_email': 'han.mdarien@gmail.com',
    'admin': 'han.mdarien@gmail.com',
    'dependencies': (
        'boto',
        'South',
        'django-extensions',
        'pytz',
    ),
    'description': 'Clash Guide App Server',
    'license': 'Private',
}