from django.views.generic import CreateView
from .models import Person


class PersonForm(CreateView):
    model = Person
    fields = ('email', 'subject', 'text')

