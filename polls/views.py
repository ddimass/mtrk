from django.shortcuts import render
from django.template.loader import get_template
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'polls/index.html')