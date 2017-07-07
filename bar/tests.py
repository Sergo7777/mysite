import datetime
from django.test import TestCase
from django.core import mail
from django.urls import reverse
from django.core import serializers
from .models import Order, Table

import json
 
class TestCalls(TestCase):
    def setUp(self):
            Table.objects.create(seats='2',
                             demensions_width='15',
                             demensions_length='15',
                             coordinates_horizontally='15',
                             coordinates_vertical='15',
                             form_table='O',)  # 2
            Order.objects.create(date='2012-12-11',
                             name='user',
                             email='serega_denisenko@mail.ru',
                             table_id=1,
                             )  # 1

    def test_home(self):
        response = self.client.get(reverse('home'), follow=True)
        self.assertTemplateUsed(response, 'bar/index.html')

    def test_send_mail_redirect(self):
        table = Table.objects.get(seats='2',
                                  demensions_width='15',
                                  demensions_length='15',
                                  coordinates_horizontally='15',
                                  coordinates_vertical='15',
                                  form_table='O',)  # 1
        response = self.client.post(
            reverse('send_mail'),
            {
                'username': 'user',
                'email': 'serega_denisenko@mail.com',
                'table_id': table.id,
                'date': '2012-12-11',
            }
        )
        self.assertRedirects(response, '/bar', 302, 301)

    def test_date_input(self):
        date = '2012-12-11'
        order = Order.objects.filter(date='2012-12-11',
                                     name='user',
                                     email='serega_denisenko@mail.ru',
                                     table_id=1, 
                                     )  # 2
        response = self.client.post(reverse('date_input'), {'date':'2012-12-11',
                                     'name':'user',
                                     'email':'serega_denisenko@mail.ru',
                                     'table_id': 1,})
        order_from_response = serializers.deserialize('json', response.content.decode())
        self.assertEqual(list(order_from_response)[0].object.id, order[0].id)