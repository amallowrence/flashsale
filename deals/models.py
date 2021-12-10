from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.

class User(AbstractUser):
  username = models.CharField(max_length = 50, primary_key=True)
  phone_no = models.CharField(max_length = 10)


class orderTable(models.Model):
    username = models.ForeignKey(to="User",to_field="username",on_delete=CASCADE)
    buyTime = models.DateField()


class dealTable(models.Model):
    dealname = models.CharField(primary_key=True,max_length=50)
    startTime = models.DateField()
    endTime = models.DateField()
    price = models.FloatField()
    quantity = models.IntegerField()
