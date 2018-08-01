from django import forms
from django.contrib.auth.models import User

from blog.models import Blogpost


class BlogpostForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title', 'body', 'published']


class UserSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self):
        user = super(UserSignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user
