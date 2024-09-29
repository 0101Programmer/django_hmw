from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

def class_templ(request):
    return render(request, 'class_template.html')


def func_templ(request):
    return render(request, 'func_template.html')
