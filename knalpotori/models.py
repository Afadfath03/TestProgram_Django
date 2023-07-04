from django.db import models
import os
# Create your models here.
class Data_Pengguna(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    wa = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    imae = models.CharField(max_length=50, blank=True, null=True)
    role = models.CharField(max_length=10, blank=True, null=True, default='pelanggan')
    status = models.CharField(max_length=10, blank=True, null=True, default='active')

    class Meta:
        db_table = 'dt_pengguna'