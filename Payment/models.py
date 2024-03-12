from django.db import models

# Create your models here.

from UserApp.models import Foydalanuvchilar
class Card(models.Model):
    card_holder = models.ForeignKey(Foydalanuvchilar,on_delete=models.CASCADE)
    card_number = models.IntegerField(unique=True)
    expired_date = models.DateTimeField(auto_now_add=True)