from django.db import models
from django.contrib.auth.models import User
import datetime

class Partage(models.Model):
    type = models.CharField(max_length=155)
    autheur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.TimeField(verbose_name="Date du partage")
    destinataire = models.EmailField(null=True)

    def save(self, type, autheur, destinataire=None):
        self['type'] = type
        self['autheur'] = autheur
        self['date'] = datetime.datetime.now()
        if destinataire is not None:
            self['destinataire'] = destinataire
        super(Partage, self).save()


class Product(models.Model):
    name = models.CharField(max_length=125)
    description = models.TextField(max_length=450)

    def get_absolute_url(self):
        return f"/products/{self.pk}/"
