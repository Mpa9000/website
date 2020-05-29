from django.shortcuts import render


def redirect(request):
    context = {}
    return render(request, 'redirect.html', context)

