import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-resumator',
    version='1.1.5',
    packages=['resumator'],
    install_requires=[
        'django-solo>=1.1.0',
        'Pillow>=3.0.0',
    ],
    include_package_data=True,
    license='MIT License',
    description='A lightweight Django app to create Web-based resumes.',
    long_description=README,
    url='https://github.com/AmmsA/django-resumator',
    author='Mustafa S',
    author_email='AmmsA@users.noreply.github.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
