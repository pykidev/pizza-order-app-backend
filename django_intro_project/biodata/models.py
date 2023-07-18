from django.db import models

class Intern(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    university = models.CharField(max_length=255)