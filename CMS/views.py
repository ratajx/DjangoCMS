from django.shortcuts import render
from django.shortcuts import redirect
from CMS.models import Site
from CMS.models import News
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    news = News.objects.all().filter(enable=True)
    return render(request, 'home.html', {'news': news})


def static_page(request, page_id):
    try:
        site = Site.objects.get(id=page_id)
    except ObjectDoesNotExist:
        site = None

    if(site is None):
        return render(request, '404.html')

    if site.only_for_log_in:
        if request.user.is_authenticated:
            return render(request, 'staticPage.html', {'pageContent': site.content})
        else:
            return redirect('/accounts/login/')
    else:
        return render(request, 'staticPage.html', {'pageContent': site.content})

def handler_404(request):
    return render(request, '404.html')
