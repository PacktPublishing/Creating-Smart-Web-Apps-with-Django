from django.contrib import admin

from blog.models import Blogpost

# Register your models here.


class BlogpostAdmin(admin.ModelAdmin):
    actions = ['publish_posts', 'unpublish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(published=True)

    def unpublish_posts(self, request, queryset):
        queryset.update(published=False)


admin.site.register(Blogpost, BlogpostAdmin)
