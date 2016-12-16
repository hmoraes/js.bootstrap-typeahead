from setuptools import setup, find_packages
import os

version = '0.0.5'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.rst')
    + '\n' +
    read('js', 'bootstrap_typeahead', 'test.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.bootstrap_typeahead',
    version=version,
    description="fanstatic twitter bootstrap typeahead.",
    long_description=long_description,
    classifiers=[],
    keywords='fanstatic twitter bootstrap ajax typeahead',
    author='Heberte Fernandes de Moraes',
    url='https://github.com/hmoraes/js.bootstrap-typeahead',
    author_email='brebete@gmail.com',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'js.jquery>=1.9.0',
        'js.bootstrap',
        'setuptools',
        ],
    entry_points={
        'fanstatic.libraries': [
            'bootstrap_typeahead = js.bootstrap_typeahead:library',
            ],
        },
    )
