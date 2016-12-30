"""DjangoCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from CMS import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^oauth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^home', views.home),
    url(r'^staticPage/(?P<page_id>\d+)/$', views.static_page),
    url(r'^news/(?P<news_id>\d+)/$', views.news_page),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^account/', views.account),
    url(r'^addComment/', views.add_comment),
    url(r'^removeComment/', views.remove_comment),
    url(r'^$', views.home),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'CMS.views.handler_404'
handler500 = 'CMS.views.handler_404'