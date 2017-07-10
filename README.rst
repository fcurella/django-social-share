Django Social Share
======================================

.. image:: https://travis-ci.org/fcurella/django-social-share.svg?branch=master
    :target: https://travis-ci.org/fcurella/django-social-share

.. image:: https://coveralls.io/repos/github/fcurella/django-social-share/badge.svg?branch=master
    :target: https://coveralls.io/github/fcurella/django-social-share?branch=master

Provides templatetags for 'Tweet This', 'Share this on Facebook', 'Share on Google+', 'Share on LinkedIn', and 'mailto://'.

Plain HTML templates_ are provided for your convenience, but you can override them to provide your own look and feel.

Installation
-------------

::

    $ pip install django-social-share

Add the app to ``INSTALLED_APPS``::

    INSTALLED_APPS += ['django_social_share']

You will also have to add ``django.core.context_processors.request`` to your ``context_processors`` list. This way the templatetags will use the correct scheme and hostname::

    TEMPLATES=[
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
            ],
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                ],
            }
        },
    ]

Usage
-----
::

  {% post_to_facebook <object_or_url> <link_text> %}
  
  {% post_to_gplus <object_or_url> <link_text> %}
  
  {% post_to_twitter <text_to_post> <object_or_url> <link_text> %}
  
  {% post_to_linkedin <subject> <object_or_url> <link_text> %}
  
  {% post_to_mail <email_subject> <text_to_post> <object_or_url> <link_text> %}
  
  {% send_email <subject> <text_to_post> <object_or_url> <link_text> %}
  
  {% post_to_reddit <text_to_post> <object_or_url> %}

``<text_to_post>`` may contain any valid Django Template code. Note that Facebook does not support this anymore.

``<object_or_url>`` is optional. If you pass a django model instance, it will use its ``get_absolute_url`` method. Additionally, if you have ``django_bitly`` installed, it will use its shortUrl on Twitter.

``<link_text>`` is also optional. It defines the text used for the ``a`` element. Defaults to 'Post to Facebook' and 'Post to Twitter'.

``<subject>`` may contain any valid Django Template code.

::

  {% post_to_twitter_url <text_to_post> <object_or_url> %}

Will add a ``tweet_url`` variable to the context, containing the URL for the Twitter sharer popup.

::

  {% post_to_facebook_url <object_or_url> %}

Will add a ``facebook_url`` variable to the context, containing the URL for the Facebook sharer popup.

::

  {% post_to_gplus_url <object_or_url> %}

Will add a ``gplus_url`` variable to the context, containing the URL for the Google+ sharer popup.

::

  {% post_to_linkedin_url <subject> <object_or_url> %}

Will add a ``linkedin_url`` variable to the context, containing the URL for the LinkedIn sharer popup.

::

  {% send_email_url <subject> <text_to_post> <object_or_url> <link_text> %}

Will add a ``mailto_url`` variable to the context, containing the URL for the ``mailto`` anchor.

::

  {% post_to_reddit_url <text> <object_or_url> %}

Will add a ``reddit_url`` variable to the context, containing the URL for the Reddit poster page.

Example::

  {% load social_share %}
  
  {% post_to_facebook object_or_url "Post to Facebook!" %}
  {% post_to_twitter "New Song: {{object.title}}. Check it out!" object_or_url "Post to Twitter" %}
  {% post_to_gplus object_or_url "Post to Google+!" %}
  {% post_to_linkedin object.title object_or_url "Post to LinkedIn" %}
  {% send_email object.title "New Song: {{object.title}}. Check it out!" object_or_url "Share via email" %}
  {% post_to_reddit "New Song: {{object.title}}" <object_or_url> %}

.. _templates:

Templates
---------

Templates are in:

* ``django_social_share/templatetags/post_to_twitter.html``
* ``django_social_share/templatetags/post_to_facebook.html``
* ``django_social_share/templatetags/post_to_gplus.html``
* ``django_social_share/templatetags/send_email.html``
* ``django_social_share/templatetags/post_to_linkedin.html``
* ``django_social_share/templatetags/post_to_reddit.html``.
  
You can override them to suit your mileage.
