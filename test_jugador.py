import unittest
from clases.jugador import Jugador

class TestJugador(unittest.TestCase):

    def test_get_nombre(self):
        jugador = Jugador("Carolyn", "X")
        self.assertEqual(jugador.get_nombre(), "Carolyn")

    def test_get_ficha(self):
        jugador = Jugador("Guada", "O")
        self.assertEqual(jugador.get_ficha(), "O")


if __name__ == "__main__":
    unittest.main()