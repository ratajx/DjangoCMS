from django import template
from CMS.models import Site
from CMS.models import Logo

register = template.Library()

@register.assignment_tag()
def getAllSites():
    return Site.objects.all().filter(enable=True)

@register.assignment_tag()
def getAllSitesForGuest():
    return Site.objects.all().filter(enable=True).filter(only_for_log_in=False)

@register.simple_tag()
def getLogo():
    return Logo.objects.first().logo

