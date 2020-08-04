import io
import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.rst'), encoding='utf-8') as fp:
    README = fp.read()

with open(os.path.join(here, 'VERSION')) as version_file:
    version = version_file.read().strip()

requirements = []
test_requirements = [
    "Django>=2.0",
]

setup(
    name="django-social-share",
    version=version,
    description="Templatetags for 'tweet this' and 'share on facebook'",
    long_description=README,
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
