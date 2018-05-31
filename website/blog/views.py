from django.http import HttpResponse, Http404
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

class BlogpostDetailView(View):
    def get(self, request, id):
        try:
            p = Blogpost.objects.get(id=id)
        except Blogpost.DoesNotExist:
            raise Http404()
        else:
            response = """
            {title} by {author}
            <br>
            ---
            <br><br>
            {body}
            """.format(title=p.title, author=p.author, body=p.body)

            return HttpResponse(response)
