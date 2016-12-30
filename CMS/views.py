from django.shortcuts import render
from django.shortcuts import redirect
from CMS.models import Site
from CMS.models import News
from django.core.exceptions import ObjectDoesNotExist
from CMS.models import Comment
from django.http import HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required


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

    comments = Comment.objects.all().filter(site=site).order_by('date')

    if site.only_for_log_in:
        if request.user.is_authenticated:
            return render(request, 'staticPage.html', {'site': site,
                                                       'pageHeader': pageHeader, 'comments': comments})
        else:
            return redirect('/accounts/login/')
    else:
        return render(request, 'staticPage.html', {'site': site,
                                                   'pageHeader': pageHeader, 'comments': comments})


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
            comments = Comment.objects.all().filter(news=news).order_by('date')
            return render(request, 'news.html', {'news': news, 'comments': comments})


@login_required(login_url='/accounts/login/')
def add_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment', '')
        news = request.POST.get('news', None)
        site = request.POST.get('site', None)

        if news is None:
            news_obj = None
            if site is None:
                return redirect('/home')
        else:
            try:
                news_obj = News.objects.get(id=news)
            except ObjectDoesNotExist:
                news_obj = None

        if site is None:
            site_obj = None
        else:
            try:
                site_obj = Site.objects.get(id=site)
            except ObjectDoesNotExist:
                site_obj = None

        comment = Comment(comment=comment, date=timezone.now(), user=request.user, news=news_obj, site=site_obj)
        comment.save()

    if news is None:
        return redirect('/staticPage/' + site)
    else:
        return redirect('/news/' + news)


@login_required(login_url='accounts/login/')
def remove_comment(request):
    if request.method == 'POST':
        id = request.POST.get('id', None)

    if id is not None:
        try:
            comment = Comment.objects.get(id=id)
        except ObjectDoesNotExist:
            comment = None

        if comment is not None:
            if comment.user == request.user:
                comment.delete()

    return HttpResponse(id)
