from django.shortcuts import render
from core.forms import FaceForm
from django.views.generic.edit import FormView, CreateView
from users.models import Profile
from django.http import HttpResponseRedirect


class faceFormView(FormView):
    template_name = 'core/face.html'
    form_class = FaceForm
    success_url = '/client/'

    def form_valid(self, form):
        super().form_valid(form)
        client = form.instance.face
        print(client.url)
        return HttpResponseRedirect(client.url)
