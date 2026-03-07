from django.test import TestCase
from datetime import date
from equipo.models import Equipo, Jugador, EquipoTrofeo
from equipo.enum import EquipoTrofeoOpcion, EquipoPais, JugadorPie,\
    JugadorPosicion
from django.core.exceptions import ValidationError

class EquipoTestCase(TestCase):
    def setUp(self):
        self.equipo = Equipo.objects.create(nombre="Mi Equipo", pais=EquipoPais.URUGUAY)

    def test_es_uruguay(self):
        self.assertTrue(self.equipo.es_uruguay())

    def test_get_jugadores(self):
        # Agrega algunos jugadores para el equipo
        Jugador.objects.create(equipo=self.equipo, nombre_completo="Jugador 1", fecha_nacimiento=date(1990, 1, 1))
        Jugador.objects.create(equipo=self.equipo, nombre_completo="Jugador 2", fecha_nacimiento=date(1995, 2, 2))
        
        self.assertEqual(self.equipo.get_jugadores().count(), 2)
        
    # MAX_LENGTH_NOMBRE = 64  # Longitud máxima permitida para el nombre
    # def test_nombre_largo(self):
    #     # Crear un nombre que exceda la longitud máxima permitida
    #     nombre_largo = "A" * (self.MAX_LENGTH_NOMBRE + 1)
    #
    #     # Utilizar assertRaises para capturar la excepción ValidationError
    #     with self.assertRaises(ValidationError):
    #         # Usar assertWarns para suprimir el traceback de la excepción
    #         with self.assertWarns(None) as context:
    #             equipo = Equipo.objects.create(nombre=nombre_largo, pais=EquipoPais.URUGUAY)
    #
    #     # Verificar que la excepción contiene un mensaje específico
    #     error_message = str(context.warning)
    #     self.assertIn("Ensure this value has at most", error_message)
    #     self.assertIn(f"{self.MAX_LENGTH_NOMBRE} characters", error_message)
        
class EquipoTrofeoTestCase(TestCase):
    def setUp(self):
        self.equipo = Equipo.objects.create(nombre="Mi Equipo", pais=EquipoPais.URUGUAY)
        self.trofeo = EquipoTrofeo.objects.create(equipo=self.equipo, 
                                                  trofeo=EquipoTrofeoOpcion.CAMPEONATO_URUGUAYO, 
                                                  cantidad=3)

    def test_str_representation(self):
        self.assertEqual(self.trofeo.trofeo, EquipoTrofeoOpcion.CAMPEONATO_URUGUAYO)

    def test_cantidad_default(self):
        trofeo_default = EquipoTrofeo.objects.create(equipo=self.equipo, 
                                                     trofeo=EquipoTrofeoOpcion.COPA_LIBERTADORES)
        self.assertEqual(trofeo_default.cantidad, 0)

class JugadorTestCase(TestCase):
    def setUp(self):
        self.equipo = Equipo.objects.create(nombre="Mi Equipo", pais=EquipoPais.URUGUAY)
        self.jugador = Jugador.objects.create(
            equipo=self.equipo,
            nombre_completo="Jugador Prueba",
            fecha_nacimiento=date(1990, 1, 1),
            altura=180.5,
            pie=JugadorPie.DERECHO,
            fichado=date(2021, 5, 10),
            fin_contrato=date(2023, 12, 31),
            posicion=JugadorPosicion.DELANTERO,
            salario=50000.0,
            valor_mercado=100000.0
        )

    def test_activo(self):
        self.assertTrue(self.jugador.activo())

    def test_get_fin_contrato(self):
        self.assertEqual(self.jugador.fin_contrato, date(2023, 12, 31))

    def test_nombre_completo_str(self):
        self.assertEqual(self.jugador.__str__(), "Jugador Prueba")

    def test_salario_valor_mercado_mayor_0(self):
        self.assertGreaterEqual(self.jugador.salario, 0)
        self.assertGreaterEqual(self.jugador.valor_mercado, 0)
