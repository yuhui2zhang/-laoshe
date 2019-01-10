from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    class Meta:
        db_table = 't_user'