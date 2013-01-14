import sys
sys.path.insert(0, 'project')
from setuptools import setup, find_packages
from metadata import metadata
from pprint import pprint

pprint(metadata)

setup(
    name = metadata['name'],
    version = metadata['version'],
    url = metadata['url'],
    license = metadata['license'],
    description = metadata['description'],
    author = metadata['author'],
    author_email = metadata['author_email'],
    packages = find_packages('.'),
    package_dir = {'': '.'},

    dependency_links = [
        ],

   install_requires = metadata['dependencies'],

    extras_require = {
        'SQLite': ["pysqlite>=2.0.3"],
        'PostgreSQL': ["psycopg>=1.1.21"],
        'PostgreSQL2': ["psycopg2>=2.0.5"],
    },

    include_package_data = True,

    entry_points = {
        'console_scripts': 'django = django.core.management:execute_from_command_line',
    },

)
