# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from django.db.models import Model

try:
    from django_bitly.templatetags.bitly import bitlify
    DJANGO_BITLY = True
except ImportError:
    DJANGO_BITLY = False

register = template.Library()


def compile_text(context, text):
    ctx = template.context.Context(context)
    return template.Template(text).render(ctx)


class MockRequest(object):
    def build_absolute_uri(self, relative_url):
        if relative_url.startswith('http'):
            return relative_url
        current_site = Site.objects.get_current()
        return '%s%s' % (current_site.domain, relative_url)


@register.inclusion_tag('django_social_share/templatetags/post_to_twitter.html', takes_context=True)
def post_to_twitter(context, text, obj_or_url=None, link_text='Post to Twitter'):
    text = compile_text(context, text)
    context['link_text'] = link_text
    request = context.get('request', MockRequest())

    if obj_or_url is not None:
        if isinstance(obj_or_url, Model):
            if DJANGO_BITLY:
                url = ' ' + bitlify(obj_or_url)
            else:
                url = ' ' + request.build_absolute_uri(obj_or_url.get_absolute_url())
        else:
            url = ' ' + request.build_absolute_uri(obj_or_url)
    else:
        url = ''
    total_lenght = len(text) + len(url)
    if total_lenght > 140:
        truncated_text = text[:(140 - len(url) - 1)] + "…"
    else:
        truncated_text = text
    context['full_text'] = truncated_text + url
    return context


@register.inclusion_tag('django_social_share/templatetags/post_to_facebook.html', takes_context=True)
def post_to_facebook(context, obj_or_url=None, link_text='Post to Facebook'):
    context['link_text'] = link_text
    request = context.get('request', MockRequest())

    if obj_or_url is not None:
        if isinstance(obj_or_url, Model):
            url = request.build_absolute_uri(obj_or_url.get_absolute_url())
        else:
            if obj_or_url.startswith('http'):
                url = obj_or_url
            else:
                url = request.build_absolute_uri(obj_or_url)
    else:
        url = None

    context.update({'url': url})
    return context
