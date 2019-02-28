from django.db import models


# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=40, default="")
    email = models.EmailField(default="")
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.name
