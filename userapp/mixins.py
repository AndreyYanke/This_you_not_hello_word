from django.contrib import auth
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

from this_you_not_hello_word.settings import LOGIN_REDIRECT_URL


class AuthAfterRegistMixin:

    def form_valid(self, form):
        self.object = form.save()
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        auth.login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())
