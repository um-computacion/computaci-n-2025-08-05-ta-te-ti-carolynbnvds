import unittest
from clases.tateti import Tateti

class TestTateti(unittest.TestCase):

    def setUp(self):
        self.juego = Tateti()

    
    def test_ganador_fila_0(self):
        self.juego.tablero.contenedor = [
            ["X", "X", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        estado = self.juego.ocupar_una_de_las_casillas(0, 2)
        self.assertEqual(estado, "GANADOR")

    def test_ganador_fila_1(self):
        self.juego.tablero.contenedor = [
            ["", "", ""],
            ["O", "O", ""],
            ["", "", ""]
        ]
        self.juego.turno = "O"
        estado = self.juego.ocupar_una_de_las_casillas(1, 2)
        self.assertEqual(estado, "GANADOR")

    def test_ganador_fila_2(self):
        self.juego.tablero.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["X", "X", ""]
        ]
        estado = self.juego.ocupar_una_de_las_casillas(2, 2)
        self.assertEqual(estado, "GANADOR")


    def test_ganador_col_0(self):
        self.juego.tablero.contenedor = [
            ["X", "", ""],
            ["X", "", ""],
            ["", "", ""]
        ]
        estado = self.juego.ocupar_una_de_las_casillas(2, 0)
        self.assertEqual(estado, "GANADOR")

    def test_ganador_col_1(self):
        self.juego.tablero.contenedor = [
            ["", "O", ""],
            ["", "O", ""],
            ["", "", ""]
        ]
        self.juego.turno = "O"
        estado = self.juego.ocupar_una_de_las_casillas(2, 1)
        self.assertEqual(estado, "GANADOR")

    def test_ganador_col_2(self):
        self.juego.tablero.contenedor = [
            ["", "", "X"],
            ["", "", "X"],
            ["", "", ""]
        ]
        estado = self.juego.ocupar_una_de_las_casillas(2, 2)
        self.assertEqual(estado, "GANADOR")

    
    def test_ganador_diag_1(self):
        self.juego.tablero.contenedor = [
            ["X", "", ""],
            ["", "X", ""],
            ["", "", ""]
        ]
        estado = self.juego.ocupar_una_de_las_casillas(2, 2)
        self.assertEqual(estado, "GANADOR")

    def test_ganador_diag_2(self):
        self.juego.tablero.contenedor = [
            ["", "", "O"],
            ["", "O", ""],
            ["", "", ""]
        ]
        self.juego.turno = "O"
        estado = self.juego.ocupar_una_de_las_casillas(2, 0)
        self.assertEqual(estado, "GANADOR")

    
    def test_empate_lleno(self):
        self.juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", ""]
        ]
        estado = self.juego.ocupar_una_de_las_casillas(2, 2)
        self.assertEqual(estado, "EMPATE")

    def test_empate_tablero_lleno(self):
        self.juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["O", "X", "X"],
            ["O", "X", "O"]
        ]
        self.assertTrue(self.juego.hay_empate())

    def test_no_empate_casilla_vacia(self):
        self.juego.tablero.contenedor = [
            ["X", "O", "X"],
            ["O", "X", ""],
            ["O", "X", "O"]
        ]
        self.assertFalse(self.juego.hay_empate())

    
    def test_turno_cambia(self):
        self.juego.ocupar_una_de_las_casillas(0, 0)
        self.assertEqual(self.juego.turno, "0")
        self.juego.ocupar_una_de_las_casillas(1, 0)
        self.assertEqual(self.juego.turno, "X")

if __name__ == "__main__":
    unittest.main()
