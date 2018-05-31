from django.http import HttpResponse
from django.views.generic import View

from blog.models import Blogpost

# Create your views here.

class BlogpostView(View):
    def get(self, request):
        posts = Blogpost.objects.all()

        response = [
            # 1: first post by John Doe
            "{id}: {title} by {author} <br>".format(id=p.id, title=p.title, author=p.author)
            for p in posts
        ]

        return HttpResponse(response)
