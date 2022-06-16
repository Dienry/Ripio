from django.test import TestCase
from coinapp.models import Coin, User, Registry
from django.utils import timezone

class CoinTest(TestCase):

    def setUp(self):
        Coin.objects.create(coin_name='Peso', creation_date=timezone.now())

    def test_coin_name_max_length(self):
        coin       = Coin.objects.get(id=1)
        max_length = coin._meta.get_field('coin_name').max_length
        
        self.assertEquals(max_length, 20)


class UserTest(TestCase):

    def setUp(self):
        Coin.objects.create(coin_name='Peso', creation_date=timezone.now())
        User.objects.create(user_name='Diego', coin=Coin.objects.get(id=1))

    def test_user_name_max_length(self):
        user       = User.objects.get(id=1)
        max_length = user._meta.get_field('user_name').max_length
        
        self.assertEquals(max_length, 200)

    def test_balance_is_default_value(self):
        user    = User.objects.get(id=1)
        balance = user.balance
        
        self.assertEquals(balance, 0.0)


class RegistryTest(TestCase):

    def setUp(self):
        Registry.objects.create(sender_name='Diego', receiver_name='Lucas', coin_used='Peso', amount=10.0, operation_date=timezone.now())

    def test_max_length(self):
        registry            = Registry.objects.get(id=1)
        sender_max_length   = registry._meta.get_field('sender_name').max_length
        receiver_max_length = registry._meta.get_field('receiver_name').max_length
        coin_max_length     = registry._meta.get_field('coin_used').max_length
        
        self.assertEquals(sender_max_length, 200)
        self.assertEquals(receiver_max_length, 200)
        self.assertEquals(coin_max_length, 20)