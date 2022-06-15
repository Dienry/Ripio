from django.db import models

class Coin(models.Model):
    coin_name     = models.CharField(max_length=20, unique=True)
    creation_date = models.DateTimeField('date created')

    def __str__(self):
        return self.coin_name

class User(models.Model): #The name is not unique, but I believe for the test we can leave this as is.
    user_name = models.CharField(max_length=200)
    balance   = models.FloatField(default=0.0)
    coin      = models.ForeignKey(Coin, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

class Registry(models.Model):
    sender_name    = models.CharField(max_length=200)
    receiver_name  = models.CharField(max_length=200)
    coin_used      = models.CharField(max_length=200)
    amount         = models.FloatField()
    operation_date = models.DateTimeField()