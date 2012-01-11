from django import template
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _ 

register = template.Library()


@register.filter(name='trans_app')  
def trans_app(value):
    """
    Utility templatetag filter to avoid double translations of application names.
    """
    return _(capfirst(value))

    

