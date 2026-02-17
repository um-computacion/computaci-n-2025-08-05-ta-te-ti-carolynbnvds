from clases.tablero import Tablero, PosNoExistenteException, PosOcupadaException

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()

    def ocupar_una_de_las_casillas(self, fil, col):
        """
        Intenta jugar en (fil, col) con el turno actual.
        Devuelve: 'OK', 'GANADOR', 'EMPATE', 'POS_INVALIDA', 'POS_OCUPADA'
        """
        try:
            self.tablero.poner_la_ficha(fil, col, self.turno)
        except PosNoExistenteException:
            print("Posicion no existente")
            return "POS_INVALIDA"
        except PosOcupadaException:
            print("Posicion ocupada")
            return "POS_OCUPADA"

        self.tablero.mostrar()

        if self.hay_ganador():
            print(f"Jugador {self.turno} gano")
            return "GANADOR"

        if self.hay_empate():
            print("Empate")
            return "EMPATE"

        self.turno = "O" if self.turno == "X" else "X"
        return "OK"

    def hay_ganador(self) -> bool:
        c = self.tablero.contenedor

        # filas
        for fila in c:
            if fila[0] != "" and fila[0] == fila[1] == fila[2]:
                return True

        # columnas
        for col in range(3):
            if c[0][col] != "" and c[0][col] == c[1][col] == c[2][col]:
                return True

        # diagonales
        if c[0][0] != "" and c[0][0] == c[1][1] == c[2][2]:
            return True
        if c[0][2] != "" and c[0][2] == c[1][1] == c[2][0]:
            return True

        return False

    def hay_empate(self) -> bool:
        for fila in self.tablero.contenedor:
            if "" in fila:
                return False
        return True
