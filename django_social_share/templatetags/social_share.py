# -*- coding: utf-8 -*-

from django import template
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

@register.inclusion_tag('django_social_share/templatetags/post_to_twitter.html', takes_context = True)
def post_to_twitter(context, text, obj_or_url=None):
    text = compile_text(context, text)
    request = context['request']

    if obj_or_url is not None:
        if isinstance(obj_or_url, Model):
            if DJANGO_BITLY:
                url = u' ' + bitlify(obj_or_url)
            else:
                url = u' ' + request.build_absolute_uri(obj_or_url.get_absolute_url())
        else:
            if obj_or_url.startswith('http'):
                url = u' ' + obj_or_url
            else:
                url = u' ' + request.build_absolute_uri(obj_or_url)
    else:
        url = ''
    total_lenght = len(text) + len(url)
    if total_lenght > 140:
        truncated_text = text[:(140 - len(url) - 1)] + u"…"
    else:
        truncated_text = text
    context['full_text'] = truncated_text + url
    return context


@register.inclusion_tag('django_social_share/templatetags/post_to_facebook.html', takes_context = True)
def post_to_facebook(context, text, obj_or_url=None):
    text = compile_text(context, text)

    request = context['request']
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

    context.update({'text': text, 'url': url})
    return context
