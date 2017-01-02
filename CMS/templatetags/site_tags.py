from django import template
from CMS.models import Site
from CMS.models import Logo
from CMS.models import Category

register = template.Library()


@register.assignment_tag()
def getAllSites(guest):
    if guest:
        return Site.objects.all().filter(enable=True).filter(only_for_log_in=False).filter(category=None)
    else:
        return Site.objects.all().filter(enable=True).filter(category=None)

@register.assignment_tag()
def getAllCategory(guest):
    if guest:
        sites = Site.objects.all().filter(enable=True).filter(only_for_log_in=False).filter(category__isnull=False)
    else:
        sites = Site.objects.all().filter(enable=True).filter(category__isnull=False)

    categorys = Category.objects.all();

    categoryMap = {}

    for category in categorys:
        categoryMap[category] = []

    for site in sites:
        tab = categoryMap.get(site.category)
        tab.append(site)
        categoryMap[site.category] = tab

    return categoryMap

@register.simple_tag()
def getLogo():
    return Logo.objects.first().logo
