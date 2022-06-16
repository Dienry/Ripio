from django.test import TestCase, Client
from django.urls import reverse
from coinapp.models import Coin, User, Registry
from django.utils import timezone

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_balance(self):
        response = self.client.get(reverse('coinapp:balance', args=('Diego',)))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'coinapp/balance.html')

    def test_balance_forbidden(self):
        response = self.client.get(reverse('coinapp:balance', args=('Lucas',)))

        self.assertEquals(response.status_code, 403)

    def test_movements(self):
        response = self.client.get(reverse('coinapp:movements', args=('Diego',)))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'coinapp/movements.html')

    def test_movements_forbidden(self):
        response = self.client.get(reverse('coinapp:balance', args=('Lucas',)))

        self.assertEquals(response.status_code, 403)

    def test_send_money(self):
        response = self.client.get(reverse('coinapp:send_money'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'coinapp/send_money.html')

    def test_save_coin_success(self):
        response = self.client.post(reverse('coinapp:save_coin'), {'coin_name': 'Peso'})
        coin = Coin.objects.get(id=1)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'coinapp/create_coin.html')
        self.assertEquals(coin.coin_name, 'Peso')