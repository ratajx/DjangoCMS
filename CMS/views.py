from django.shortcuts import render
from CMS.models import Site
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    sites = Site.objects.all()
    return render(request, 'home.html')

@login_required
def staticPage(request, page_id):
    pageContent = Site.objects.get(id=page_id).content
    return render(request, 'staticPage.html', {'pageContent' : pageContent})