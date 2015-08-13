from django.db import models

# Create your models here.


class Doctor(models.Model):
    username = models.CharField(primary_key=True, max_length=50)
    doctor_id = models.IntegerField()
    is_doctor = models.BooleanField()
    is_staff = models.BooleanField()
    access_token = models.CharField(max_length=100)
    refresh_token = models.CharField(max_length=100)