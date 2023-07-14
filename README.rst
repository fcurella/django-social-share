Django Social Share
======================================

.. image:: https://github.com/fcurella/django-social-share/workflows/Python%20build/badge.svg

.. image:: https://coveralls.io/repos/github/fcurella/django-social-share/badge.svg?branch=master
    :target: https://coveralls.io/github/fcurella/django-social-share?branch=master

Provides templatetags for:

* 'Tweet This'
* 'Share this on Facebook'
* 'Share on Google+'
* 'Share on LinkedIn'
* 'Share on Telegram'
* 'Share on WhatsApp'
* 'mailto://'.
* 'Save to Pinterest'
* 'Copy to Clipboard'

Plain HTML templates_ are provided for your convenience, but you can override them to provide your own look and feel.

Installation
-------------

::

    $ python -m pip install django-social-share

Add the app to ``INSTALLED_APPS``::

    INSTALLED_APPS += ['django_social_share']

You will also have to add ``django.template.context_processors.request`` to your ``context_processors`` list. This way the templatetags will use the correct scheme and hostname::

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
    
Note in most cases sharing will not work if you are using ``localhost`` or your domain is otherwise not accessible from the public internet. For testing local development, you can use a service like ngrok_, and set your `Site instance <https://docs.djangoproject.com/en/3.0/ref/contrib/sites/>`_'s ``domain`` to the hostname provided by ``ngrok``.

.. _ngrok: https://ngrok.com/

Usage
-----

First, add ``{% load social_share %}`` to your HTML template.
This tag should be placed at the top of most of your HTML document and should come before any other template tag unless otherwise.

`django-social-share` provides two types of template tags: "snippet" tags and "context" tags.

Snippet Tags
~~~~~~~~~~~~

Snippet tags returns HTML that you can just drop in your templates. This snippets are customizable, see templates_
.

Available Snippets Tags:

::

  {% post_to_facebook <object_or_url> <link_text> <link_class> %}
  
  {% post_to_gplus <object_or_url> <link_text> <link_class> %}
  
  {% post_to_twitter <text_to_post> <object_or_url> <link_text> <link_class> %}
  
  {% post_to_linkedin <object_or_url> <link_class> %}
    
  {% post_to_reddit <text_to_post> <object_or_url> <link_text> <link_class> %}

  {% post_to_telegram <text_to_post> <object_or_url> <link_text>  <link_class> %}

  {% post_to_whatsapp <object_or_url> <link_text> <link_class> %}

  {% save_to_pinterest <object_or_url>  <link_class> %}

  {% add_pinterest_script %}

``<text_to_post>`` may contain any valid Django Template code. Note that Facebook does not support this anymore.

``<object_or_url>`` is optional (except Telegram). If you pass a django model instance, it will use its ``get_absolute_url`` method. Additionally, if you have ``django_bitly`` installed, it will use its shortUrl on Twitter.

``<link_text>`` is also optional. It defines the text used for the ``a`` element. Defaults to 'Post to Facebook' and 'Post to Twitter'.

Example::

  {% load social_share %}
  
  {% post_to_facebook object_or_url "Post to Facebook!" %}
  {% post_to_twitter "New Song: {{object.title}}. Check it out!" object_or_url "Post to Twitter" %}
  {% post_to_gplus object_or_url "Post to Google+!" %}
  {% post_to_linkedin object_or_url %}
  {% send_email object.title "New Song: {{object.title}}. Check it out!" object_or_url "Share via email" %}
  {% post_to_reddit "New Song: {{object.title}}" <object_or_url> %}
  {% post_to_telegram "New Song: {{object.title}}" <object_or_url> %}
  {% post_to_whatsapp object_or_url "Share via WhatsApp" %}
  {% save_to_pinterest object_or_url %}
  {% add_pinterest_script %} // Required for save_to_pinterest. Add to the end of body tag.

.. _templates:

Templates
---------

Templates for snippet tags are in:

* ``django_social_share/templatetags/post_to_twitter.html``
* ``django_social_share/templatetags/post_to_facebook.html``
* ``django_social_share/templatetags/post_to_gplus.html``
* ``django_social_share/templatetags/send_email.html``
* ``django_social_share/templatetags/post_to_linkedin.html``
* ``django_social_share/templatetags/post_to_reddit.html``.
* ``django_social_share/templatetags/post_to_telegram.html``.
* ``django_social_share/templatetags/post_to_whatsapp.html``.
* ``django_social_share/templatetags/save_to_pinterest.html``.
* ``django_social_share/templatetags/pinterest_script.html``.
* ``django_social_share/templatetags/copy_to_clipboard.html``.
* ``django_social_share/templatetags/copy_script.html``.
  
You can override them to suit your mileage.

Context Tags
~~~~~~~~~~~~

Context Tags work by adding a variable to your template's context. This variable will containg just the URL to service's share feature, which you can use into your template as you wish.

Available Context Tags:

============================================================================= =================
Tag example                                                                   Variable name
============================================================================= =================
``{% post_to_twitter_url <text_to_post> <object_or_url> %}``                  ``tweet_url``
``{% post_to_facebook_url <object_or_url> %}``                                ``facebook_url``
``{% post_to_gplus_url <object_or_url> %}``                                   ``gplus_url``
``{% send_email_url <subject> <text_to_post> <object_or_url> <link_text> %}`` ``mailto_url``
``{% post_to_reddit_url <text> <object_or_url> %}``                           ``reddit_url``
``{% post_to_telegram <text> <object_or_url> %}``                             ``telegram_url``
``{% post_to_whatsapp_url <object_or_url> %}``                                ``whatsapp_url``
``{% save_to_pinterest_url <object_or_url> %}``                               ``pinterest_url``
``{% copy_to_clipboard <object_or_url> <link_text> <link_class> %}``          ``copy_url``

``<text_to_post>`` may contain any valid Django Template code. Note that Facebook does not support this anymore.

``<object_or_url>`` is optional (except Telegram). If you pass a django model instance, it will use its ``get_absolute_url`` method. Additionally, if you have ``django_bitly`` installed, it will use its shortUrl on Twitter.

``<link_text>`` is also optional. It defines the text used for the ``a`` element. Defaults to 'Post to Facebook' and 'Post to Twitter'.

Example::

  {% load social_share %}
  
  {% post_to_facebook object_or_url "Post to Facebook!" %}
  {% post_to_twitter "New Song: {{object.title}}. Check it out!" object_or_url "Post to Twitter" %}
  {% post_to_gplus object_or_url "Post to Google+!" %}
  {% post_to_linkedin object_or_url %}
  {% send_email object.title "New Song: {{object.title}}. Check it out!" object_or_url "Share via email" %}
  {% post_to_reddit "New Song: {{object.title}}" <object_or_url> %}
  {% post_to_telegram "New Song: {{object.title}}" <object_or_url> %}
  {% post_to_whatsapp object_or_url "Share via WhatsApp" %}
  {% save_to_pinterest object_or_url %}
  {% add_pinterest_script %} // Required for save_to_pinterest. Add to the end of body tag.
  {% copy_to_clipboard object_or_url "Copy to clipboard!" %}
  {% add_copy_script %} // Required for copy_to_clipboard. Add to the end of body tag.

Issues
------

If you have any issues, please use `GitHub's issues <https://github.com/fcurella/django-social-share/issues>`_.
Please refrain from emailing the author.
