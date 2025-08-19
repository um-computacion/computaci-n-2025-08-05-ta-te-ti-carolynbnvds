import unittest
from clases.tablero import Tablero, PosOcupadaException, PosNoExistenteException

class TestTablero(unittest.TestCase):

    def setUp(self):
        self.tablero = Tablero()

    def test_poner_ficha_valida(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        self.assertEqual(self.tablero.contenedor[0][0], "X")

    def test_poner_ficha_posicion_ocupada(self):
        self.tablero.poner_la_ficha(0, 0, "X")
        with self.assertRaises(PosOcupadaException):
            self.tablero.poner_la_ficha(0, 0, "O")

    def test_poner_ficha_posicion_no_existente(self):
        with self.assertRaises(PosNoExistenteException):
            self.tablero.poner_la_ficha(3, 0, "X")

    def test_mostrar_no_rompe(self):
        try:
            self.tablero.mostrar()
        except Exception as e:
            self.fail(f"mostrar() lanzó excepción: {e}")


if __name__ == "__main__":
    unittest.main()