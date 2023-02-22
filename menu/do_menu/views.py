from django.shortcuts import render
from .models import Menu


def index(request, category=None):
    template = "do_menu/index.html"
    return render(request, template, context={'category': category}, )
