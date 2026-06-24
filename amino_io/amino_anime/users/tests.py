from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class SignupPageTests(TestCase):
    def test_signup_page_renders(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Регистрация')
        self.assertContains(response, 'Зарегистрироваться')

    def test_signup_post_creates_user(self):
        response = self.client.post(
            reverse('account_signup'),
            {
                'username': 'newuser',
                'email': 'newuser@example.com',
                'password1': 'StrongPass123',
                'password2': 'StrongPass123',
            },
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())
