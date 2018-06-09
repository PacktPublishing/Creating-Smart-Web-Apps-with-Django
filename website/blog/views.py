from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse

from blog.models import Blogpost
from blog.forms import BlogpostForm

# Create your views here.

class BlogpostView(TemplateView):
    template_name = 'blog/index.html'

    def get(self, request):
        posts = Blogpost.objects.all()

        response = [{
            'id': p.id,
            'title': p.title,
            'author': p.author,
        } for p in posts]

        return self.render_to_response({'posts': response})


class BlogpostDetailView(TemplateView):
    template_name = 'blog/detail.html'

    def get(self, request, id):
        try:
            p = Blogpost.objects.get(id=id)
        except Blogpost.DoesNotExist:
            raise Http404()
        else:
            context = {
                'title': p.title,
                'author': p.author,
                'body': p.body,
            }

            return self.render_to_response(context)


class BlogpostCreateView(TemplateView):
    template_name = 'blog/create.html'

    def get(self, request):
        form = BlogpostForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = BlogpostForm(data=request.POST)
        if not form.is_valid():
            return self.render_to_response({'errors': form.errors})

        blogpost = form.save()

        return HttpResponseRedirect(reverse('posts-detail', kwargs={'id': blogpost.id}))
