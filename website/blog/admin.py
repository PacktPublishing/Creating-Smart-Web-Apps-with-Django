from django.contrib import admin

from blog.models import Blogpost

# Register your models here.


class BlogpostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blogpost, BlogpostAdmin)
