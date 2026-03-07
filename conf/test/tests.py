from django.test import TestCase

class ConfTestCase(TestCase):
    def test_servidor_activo(self):
        response = self.client.get('https://novulnerable.proyectoprogsd.com/')
        self.assertEqual(response.status_code, 200)