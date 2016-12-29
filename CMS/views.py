from django.shortcuts import render
from django.shortcuts import redirect
from CMS.models import Site
from CMS.models import News
from django.core.exceptions import ObjectDoesNotExist
from CMS.models import Comment


def home(request):
    news = News.objects.all().filter(enable=True)
    return render(request, 'home.html', {'news': news})


def static_page(request, page_id):
    try:
        site = Site.objects.get(id=page_id)
    except ObjectDoesNotExist:
        site = None

    if site is None:
        return render(request, '404.html')

    if site.main_header_of_site == '':
        pageHeader = site.name
    else:
        pageHeader = site.main_header_of_site

    if site.only_for_log_in:
        if request.user.is_authenticated:
            return render(request, 'staticPage.html', {'pageContent': site.content,
                                                       'pageHeader': pageHeader})
        else:
            return redirect('/accounts/login/')
    else:
        return render(request, 'staticPage.html', {'pageContent': site.content,
                                                   'pageHeader': pageHeader})


def handler_404(request):
    return render(request, '404.html')


def account(request):
    if request.user.is_authenticated:
        comments = Comment.objects.all().filter(user=request.user)
        return render(request, 'account.html', {'comments': comments})
    else:
        return redirect('/accounts/login/')


def news_page(request, news_id):
    try:
        news = News.objects.get(id=news_id)
    except ObjectDoesNotExist:
        news = None

    if news is None:
        return render(request, '404.html')
    else:
        if not news.enable:
            return render(request, '404.html')
        else:
            return render(request, 'news.html', {'news': news})
