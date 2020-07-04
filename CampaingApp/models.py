from django.contrib.auth.models import User
import uuid

from django.db import models


class Profile(models.Model):
    user    = models.OneToOneField(User, on_delete=models.PROTECT)
    


class Campaing(models.Model):
    id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title   = models.CharField(max_length=350, null=False, blank=False)
    master  = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title


class Race(models.Model):
    id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name    = models.CharField(max_length=350, null=False, blank=False)
    desc    = models.TextField()

    def __str__(self):
        return self.name


class Pj(models.Model):
    id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name    = models.CharField(max_length=350, null=False, blank=False)
    user    = models.ForeignKey(User, on_delete=models.PROTECT)
    race    = models.ForeignKey(Race, on_delete=models.PROTECT)

    def __str__(self):
        return "Nombre: {} /// Usuario: {}".format(self.name, self.user)


class Quest(models.Model):
    id      = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title   = models.CharField(max_length=350, null=False, blank=False)
    desc    = models.CharField(max_length=350, null=False, blank=False)
    camp    = models.ForeignKey(Campaing, related_name="questo", on_delete=models.PROTECT)
    participants    = models.ManyToManyField(Pj)

    def __str__(self):
        return "Master: {} /// Campaña: {} /// Quest: {}".format(self.camp.master.username, self.camp.title, self.title)