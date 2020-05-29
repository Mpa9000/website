from django.shortcuts import render


def stories(request):
    context = {}
    return render(request, 'stories.html', context)
