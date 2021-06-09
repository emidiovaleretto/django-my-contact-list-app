from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    to_show = models.BooleanField(default=True)

    def __str__(self):
        return self.name
