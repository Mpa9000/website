from django.shortcuts import render
from django.http import HttpResponse


def pages(request):
    context = {}
    return render(request, 'allpages.html', context)
