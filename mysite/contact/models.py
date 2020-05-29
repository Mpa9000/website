from django.db import models


class Person(models.Model):
    email = models.CharField(max_length=130)
    subject = models.CharField(max_length=130)
    text = models.CharField(max_length=350)

