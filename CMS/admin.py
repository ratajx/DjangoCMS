from django.contrib import admin
from CMS.models import Book
from CMS.models import Site

class BookAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'description', 'published_date', 'price', 'stock')

class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'only_log_in', 'content')

admin.site.register(Book, BookAdmin);
admin.site.register(Site, SiteAdmin);