from django.contrib import admin
from CMS.models import Site
from CMS.models import Category
from CMS.models import News
from CMS.models import Comment
from CMS.models import Logo


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'main_header_of_site', 'only_for_log_in', 'enable')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'full_text', 'enable', 'date')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'comment', 'date')

    def has_add_permission(self, request, obj=None):
        return False

class LogoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

admin.site.register(Site, SiteAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Logo,LogoAdmin)
