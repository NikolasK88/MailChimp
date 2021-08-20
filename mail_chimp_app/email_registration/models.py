from django.db import models
from django.contrib.auth.models import User


class InfoModel(models.Model):
    fullname = models.CharField(max_length=150, blank=True, null=True)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    total_employees = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = 'InfoModel'
        verbose_name_plural = 'InfoModels'

    def __str__(self):
        return self.email




