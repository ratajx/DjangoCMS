from django import template
from CMS.models import Site

register = template.Library()

@register.assignment_tag()
def getAllSites():
    return Site.objects.all().filter(enable=True)

@register.assignment_tag()
def getAllSitesForGuest():
    return Site.objects.all().filter(enable=True).filter(only_log_in=False)

