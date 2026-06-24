from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Plant


class PlantAgentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='gardener', password='secret123')

    def test_plant_list_requires_login(self):
        response = self.client.get(reverse('plant_agent:list'))
        self.assertEqual(response.status_code, 302)

    def test_user_can_create_plant(self):
        self.client.login(username='gardener', password='secret123')
        response = self.client.post(
            reverse('plant_agent:create'),
            {
                'name': 'Aloe Vera',
                'species': 'Aloe',
                'water_every_days': 10,
                'notes': 'Sunny spot',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Plant.objects.filter(name='Aloe Vera', owner=self.user).exists())
