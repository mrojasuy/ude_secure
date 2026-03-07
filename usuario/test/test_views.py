from django.test import TestCase
from django.urls import reverse
from usuario.models import Hincha, Dirigente
from perfil.models import Perfil
from equipo.models import Equipo

class VistasTestCase(TestCase):
    def setUp(self):
        # Crear un usuario para autenticación
        self.user_uno = Perfil.objects.create_user(username='testuser_uno', password='testpassword')
        self.user_dos = Perfil.objects.create_user(username='testuser_dos', password='testpassword')
        self.equipo = Equipo.objects.create(nombre="Equipo Local")
        # Crear instancias de los modelos para las pruebas
        self.hincha = Hincha.objects.create(usuario=self.user_uno, 
                                            nombre='John', 
                                            apellido='Doe', 
                                            email='john@example.com'
                                            )
        self.hincha.equipos.add(self.equipo)
        self.dirigente = Dirigente.objects.create(usuario=self.user_dos, 
                                                  nombre='Jane', 
                                                  apellido='Smith', 
                                                  email='jane@example.com',
                                                  equipo=self.equipo)



    def test_detalle_hincha_view_acceso_no_autenticado(self):
        url = reverse('usuario:detalle', kwargs={'pk': self.hincha.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Debe redirigirse al inicio de sesión
    #
    def test_editar_hincha_view_acceso_no_autenticado(self):
        url = reverse('usuario:editar-hincha', kwargs={'pk': self.hincha.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        
    def test_detalle_dirigente_view_acceso_no_autenticado(self):
        url = reverse('usuario:detalle', kwargs={'pk': self.dirigente.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Debe redirigirse al inicio de sesión
    #
    def test_editar_dirigente_view_acceso_no_autenticado(self):
        url = reverse('usuario:editar-dirigente', kwargs={'pk': self.dirigente.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

