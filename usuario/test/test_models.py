from django.test import TestCase
from django.contrib.auth.models import User
from equipo.models import Equipo
from usuario.models import Persona, TokenActivacion, Hincha, Dirigente
from usuario.enum import PersonaRol
from perfil.models import Perfil

class UsuarioTestCase(TestCase):
    def setUp(self):
        self.user = Perfil.objects.create(username="testuser")
        self.equipo = Equipo.objects.create(nombre="Equipo A")

    def test_persona_get_nombre_apellido(self):
        persona = Persona.objects.create(
            usuario=self.user,
            nombre="John",
            apellido="Doe",
            email="john@example.com",
        )
        self.assertEqual(persona.get_nombre_apellido(), "John Doe")

    def test_persona_creacion_token(self):
        persona = Persona.objects.create(
            usuario=self.user,
            nombre="John",
            apellido="Doe",
            email="john@example.com",
        )
        nuevo_token = "abcd1234"
        persona.crear_token(nuevo_token)
        token_activacion = TokenActivacion.objects.get(user=self.user)
        self.assertEqual(token_activacion.token, nuevo_token)

    def test_hincha_es_dirigente(self):
        hincha = Hincha.objects.create(
            usuario=self.user,
            nombre="Hincha",
            apellido="Uno",
            email="hincha@example.com",
        )
        self.assertFalse(hincha.es_dirigente())

    def test_dirigente_es_dirigente(self):
        dirigente = Dirigente.objects.create(
            usuario=self.user,
            nombre="Dirigente",
            apellido="Uno",
            email="dirigente@example.com",
            equipo=self.equipo
        )
        self.assertTrue(dirigente.es_dirigente())

    def test_token_activacion(self):
        token = TokenActivacion.objects.create(
            user=self.user,
            token="token123",
            usado=False
        )
        self.assertFalse(token.usado)

    def test_hincha_get_id_equipos(self):
        hincha = Hincha.objects.create(
            usuario=self.user,
            nombre="Hincha",
            apellido="Dos",
            email="hincha@example.com",
        )
        hincha.equipos.add(self.equipo)
        self.assertEqual(hincha.get_id_equipos(), [self.equipo.pk])

  
