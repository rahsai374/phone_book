from django.db import models
from helpers.models import AbstractBaseModel
from django.contrib.auth.models import User

class Contact(AbstractBaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=False, unique=True)
    phone_number = models.CharField(max_length=10)
