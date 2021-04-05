from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Notification(models.Model):
  location = models.CharField(max_length=255)
  phone_number = PhoneNumberField()
