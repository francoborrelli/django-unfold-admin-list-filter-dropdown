# encoding: utf-8

import os
from setuptools import find_packages, setup

VERSION = '1.0.4'

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

description = 'Use dropdowns in Django admin list filter'

setup(
    name='django-unfold-admin-list-filter-dropdown',
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description=description,
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/francoborrelli/django-unfold-admin-list-filter-dropdown',
    download_url='https://github.com/francoborrelli/django-unfold-admin-list-filter-dropdow/archive/%s.zip' % VERSION,
    author='Franco Borrelli',
    author_email="francoborrelli96@gmail.com",
    keywords=['django', 'admin', 'filter', 'dropdown', 'unfold', 'django-unfold'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
