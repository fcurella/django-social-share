Django Social Share
======================================

Provides tempatetags for 'Tweet This' and 'Share this on Facebook'

::

  INSTALLED_APPS += ['django_social_share']


In your template::

  {% load social_share %}
  
  {% post_to_facebook "text" object_or_url %}
  {% post_to_twitter "text" object_or_url %}

``object_or_url`` is optional. If you pass a django model instance, it will use its ``get_absolute_url`` method. Additionally, if you have ``django_bitly`` installed, it will use its shortUrl on Twitter.
