from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .contactform import PersonForm


@login_required(login_url='singin')
def contact(request):
    form = PersonForm
    context = {'form': form}

    return render(request, 'contact.html', context)


def sendemail(request):
    subject = request.POST.get('subject', ''),
    message = request.POST.get('message', ''),
    from_email = request.POST.get('from_email', ''),

    send_mail(subject, message, from_email, ['marcplanasalmirall@gmail.com'])
