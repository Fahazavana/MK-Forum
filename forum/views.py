from django.shortcuts import render
from django.views.generic import TemplateView


# Home View
class indexView(TemplateView):
    template_name = "base.html"
