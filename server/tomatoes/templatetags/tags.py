from django import template
register = template.Library()

@register.simple_tag
def dict_key_lookup(dictionnary, key):
   return dictionnary.get(key, '')
