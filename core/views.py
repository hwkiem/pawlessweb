from django.shortcuts import render
from core.forms import FaceForm
from django.views.generic.edit import FormView
from users.models import Profile


class faceFormView(FormView):
    template_name = 'core/face.html'
    form_class = FaceForm
    success_url = '/client/'

    def form_valid(self, form):
        client = form.instance.face
        return super().form_valid(form)

