#!/usr/bin/env python
import sys

from django.conf import settings

settings.configure(
    SITE_ID=1,
    DATABASES={
        'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory;'}
    },
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.sessions',
        'django.contrib.contenttypes',
        'django.contrib.sites',
        'django_social_share',
        'django_social_share.tests',
    ],
)


def runtests(*test_args):
    import django
    try:
        django.setup()  # Django 1.7+
    except AttributeError:
        pass
    import django.test.utils
    runner_class = django.test.utils.get_runner(settings)
    test_runner = runner_class(verbosity=1, interactive=True)
    failures = test_runner.run_tests(['django_social_share'])
    sys.exit(failures)

if __name__ == '__main__':
    runtests()
