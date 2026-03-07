from django.test import TestCase
from equipo.models import Equipo, Jugador
from campeonato.models import Partido, Gol
from datetime import date

class PartidoModelTestCase(TestCase):
    def setUp(self):
        self.equipo_local = Equipo.objects.create(nombre="Equipo Local")
        self.equipo_visitante = Equipo.objects.create(nombre="Equipo Visitante")
        self.jugador = Jugador.objects.create(equipo=self.equipo_local, 
                                              nombre_completo="Jugador de Prueba",
                                              fecha_nacimiento=date(1990, 1, 1))

    def test_obtener_resultado(self):
        partido = Partido.objects.create(
            fecha=date.today(),
            equipo_local=self.equipo_local,
            equipo_visitante=self.equipo_visitante,
            goles_local=2,
            goles_visitante=1
        )
        resultado = partido.get_resultado()
        self.assertEqual(resultado, "2 - 1")

    def test_obtener_goles_equipo_local(self):
        partido = Partido.objects.create(
            fecha=date.today(),
            equipo_local=self.equipo_local,
            equipo_visitante=self.equipo_visitante
        )
        gol = Gol.objects.create(jugador=self.jugador, partido=partido, minuto=10)
        lista_goles = partido.obtener_goles_equipo_local()
        self.assertEqual(lista_goles, ['{0} (10)'.format(self.jugador)])

    def test_actualizar_jugadores_goles(self):
        partido = Partido.objects.create(
            fecha=date.today(),
            equipo_local=self.equipo_local,
            equipo_visitante=self.equipo_visitante
        )
        gol = Gol.objects.create(jugador=self.jugador, partido=partido, minuto=10)
        partido.actualizar_jugadores_goles()
        jugadores_goles = partido.jugadores_goles.all()
        self.assertEqual(list(jugadores_goles), [self.jugador])

class GolModelTestCase(TestCase):
    def setUp(self):
        self.equipo = Equipo.objects.create(nombre="Equipo de Prueba")
        self.jugador = Jugador.objects.create(equipo=self.equipo, nombre_completo="Jugador 1", fecha_nacimiento=date(1990, 1, 1))


        self.partido = Partido.objects.create(
            fecha=date.today(),
            equipo_local=self.equipo,
            equipo_visitante=self.equipo,
            goles_local=2,
            goles_visitante=1
        )

    def test_str_representation(self):
        gol = Gol.objects.create(jugador=self.jugador, partido=self.partido, minuto=10)
        str_representation = str(gol)
        self.assertEqual(str_representation, '{0} - {1}'.format(self.jugador, self.partido))
