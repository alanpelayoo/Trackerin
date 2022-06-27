from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) #none delete products if user is deleted
    name = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=False, blank=False, default='Abierto')
    category = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)
    in_m = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    out_m = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    def __str__(self):  #Method to return name
        return self.name


class Movement(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE,null=True) #One product can have multiple reviews
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    authorized = models.BooleanField(default=False)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):  #Method to return name
        return str(self.name) #return must be a string

