from django.shortcuts import render
from core.forms import FaceForm
from django.views.generic.edit import FormView


class faceFormView(FormView):
    template_name = 'core/face.html'
    form_class = FaceForm
    success_url = 'feed-home'

    def form_valid(self, form):
        print(form.instance.face.name)

        return super().form_valid(form)
