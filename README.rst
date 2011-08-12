Django Social Share
======================================

Provides tempatetags for 'Tweet This' and 'Share this on Facebook'

::

  INSTALLED_APPS += ['django_social_share']


In your template::

  {% load social_share %}
  
  {% post_to_facebook "New Song: {{object.title}}. Check it out!" object_or_url %}
  {% post_to_twitter "New Song: {{object.title}}. Check it out!" object_or_url %}

The text may contain any valid Django Template code.

``object_or_url`` is optional. If you pass a django model instance, it will use its ``get_absolute_url`` method. Additionally, if you have ``django_bitly`` installed, it will use its shortUrl on Twitter.


Templates are in ``django_social_share/templatetags/post_to_twitter.html`` and ``django_social_share/templatetags/post_to_facebook.html``. You can override them to suit your mileage.