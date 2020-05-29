from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='singin')
def home(request):
    context = {}
    return render(request, 'home.html', context)
