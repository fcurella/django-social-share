Django Social Share
======================================

Provides tempatetags for 'Tweet This' and 'Share this on Facebook'.

Installation
-------------

::

    $ pip install django-social-share

Add the app to ``INSTALLED_APPS``::

  INSTALLED_APPS += ['django_social_share']

It's recommended to add ``django.core.context_processors.request`` to your `` TEMPLATE_CONTEXT_PROCESSORS`` list. This way the templatetags will use the correct scheme and hostname.

If ``django.core.context_processors.request`` is not present, it will simply concatenate the current site's domain (from ``django.contrib.sites``) and the object's relative URL together.

Usage
-----
::

  {% post_to_facebook <object_or_url> <link_text> %}

  {% post_to_twitter <text_to_post> <object_or_url> <link_text> %}

``<text_to_post>`` may contain any valid Django Template code. Note that Facebook does not support this anymore.

``<object_or_url>`` is optional. If you pass a django model instance, it will use its ``get_absolute_url`` method. Additionally, if you have ``django_bitly`` installed, it will use its shortUrl on Twitter.

``<link_text>`` is also optional. It defines the text used for the ``a`` element. Defaults to 'Post to Facebook' and 'Post to Twitter'

::

  {% post_to_twitter_url <text_to_post> <object_or_url> %}

Will add a ``tweet_url`` variable to the context, containing the URL for the Twitter sharer popup.

::

  {% post_to_facebook_url <object_or_url> %}

Will add a ``facebook_url`` variable to the context, containing the URL for the Facebook sharer popup.

Example::

  {% load social_share %}
  
  {% post_to_facebook object_or_url "Post to Facebook!" %}
  {% post_to_twitter "New Song: {{object.title}}. Check it out!" object_or_url "Post to Twitter" %}

Templates are in ``django_social_share/templatetags/post_to_twitter.html`` and ``django_social_share/templatetags/post_to_facebook.html``. You can override them to suit your mileage.
