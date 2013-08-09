from setuptools import setup

VERSION = '0.0.1dev'

setup(
    name='pkgconfig',
    version=VERSION,
    author='Matthias Vogelgesang',
    author_email='matthias.vogelgesang@gmail.com',
    url='http://github.com/matze/pkgconfig',
    license='MIT',
    packages=['pkgconfig'],
    description="Interface Python with pkg-config",
    long_description=open('README.md').read(),
    tests_require=['nose'],
    test_suite='test',
)