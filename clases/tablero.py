class PosOcupadaException(Exception):
    pass
class PosNoExistenteException(Exception):   
    pass
class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def poner_la_ficha(self, fil, col, ficha):
        if fil < 0 or fil > 2 or col < 0 or col > 2:
            raise PosNoExistenteException("Posicion no existente!")
        if self.contenedor[fil][col] == "":
            self.contenedor[fil][col] = ficha
        else:
            raise PosOcupadaException("Posicion ocupada!")
        

    def mostrar(self):
        for fila in self.contenedor:
            print("-" * 16)
            print("   |   ".join(fila))
            print("-" * 16)