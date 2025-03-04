#rom django.shortcuts import render
from django.views.generic import TemplateView
#rom .views import  TemplateView
# Create your views here.


class homeview(TemplateView):
    template_name='home.html'