from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Division(models.Model):
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    name_bn = models.CharField(max_length=100, unique=True, null=True, blank=True)
    lat = models.CharField(max_length=100, null=True, blank=True)
    long = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    name_bn = models.CharField(max_length=100, unique=True, null=True, blank=True)
    lat = models.CharField(max_length=100, null=True, blank=True)
    long = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name



class Upazila(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,  null=True, blank=True)
    name_bn = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Union(models.Model):
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,  null=True, blank=True)
    name_bn = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name