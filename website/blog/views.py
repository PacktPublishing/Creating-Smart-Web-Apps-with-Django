from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Blogpost
from blog.forms import BlogpostForm, UserSignupForm
from blog.tasks import send_welcome_mail

# Create your views here.

class BlogpostView(TemplateView):
    template_name = 'blog/index.html'

    def get(self, request):
        posts = Blogpost.objects.all().order_by('id')

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


class BlogpostCreateView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/create.html'

    def get(self, request):
        form = BlogpostForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = BlogpostForm(data=request.POST)
        if not form.is_valid():
            return self.render_to_response({'errors': form.errors})

        blogpost = form.save(commit=False)
        blogpost.user = request.user
        blogpost.save()

        return HttpResponseRedirect(reverse('posts-detail', kwargs={'id': blogpost.id}))


class BlogpostEditView(LoginRequiredMixin, TemplateView):
    template_name = 'blog/edit.html'

    def get(self, request, id):
        # Equivalent to executing Blogpost.objects.get(id=id)
        blogpost = get_object_or_404(Blogpost, id=id)

        if blogpost.user != request.user:
            raise Http404

        form = BlogpostForm(instance=blogpost)

        return self.render_to_response({'form': form, 'id': id})

    def post(self, request, id):
        blogpost = get_object_or_404(Blogpost, id=id)

        if blogpost.user != request.user:
            raise Http404

        form = BlogpostForm(data=request.POST, instance=blogpost)
        if not form.is_valid():
            return self.render_to_response({'errors': form.errors})

        blogpost = form.save()

        return HttpResponseRedirect(reverse('posts-detail', kwargs={'id': blogpost.id}))


class SignupView(TemplateView):
    template_name = 'blog/signup.html'

    def get(self, request):
        form = UserSignupForm()
        return self.render_to_response({'form': form})

    def post(self, request):
        form = UserSignupForm(data=request.POST)
        if not form.is_valid():
            return self.render_to_response({'form': form})

        user = form.save()

        send_welcome_mail.delay(user.email)

        return HttpResponseRedirect(reverse('posts'))
