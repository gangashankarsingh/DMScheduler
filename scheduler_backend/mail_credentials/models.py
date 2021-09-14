from django.db import models
from fernet_fields import EncryptedTextField

# Create your models here.



class RecepientContacts(models.Model):
    email_id = models.EmailField(max_length=254, primary_key=True)
    description = models.CharField(max_length=100)

class Authentication(models.Model):
    key_id = models.CharField(max_length=10, primary_key=True)
    email_id = models.EmailField(max_length=254)
    authenticator = EncryptedTextField()
    recepients = models.ManyToManyField(RecepientContacts)


