import os
from setuptools import setup, find_packages

VERSION = '1.2.0'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


requirements = []
test_requirements = [
    "Django>=1.7",
]

setup(
    name="django-social-share",
    version=VERSION,
    description="Templatetags for 'tweet this' and 'share on facebook'",
    long_description=read('README.rst'),
    url='https://github.com/fcurella/django-social-share',
    license='MIT',
    author='Flavio Curella',
    author_email='flavio.curella@curella.org',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='django_social_share.tests.runtests.runtests'
)
