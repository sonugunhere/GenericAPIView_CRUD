from django.db import models

# Create your models here.
class Trade(models.Model):
    type_choices = [('buy', 'Buy'), ('sell', 'Sell')]
    type = models.CharField(max_length=4, choices=type_choices)
    user_id = models.IntegerField()
    symbol = models.CharField(max_length=10)
    shares = models.IntegerField()
    price = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)