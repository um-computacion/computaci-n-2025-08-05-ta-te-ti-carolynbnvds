class Jugador:
    def __init__(self, nombre: str, ficha: str): 
        self.nombre = nombre.strip()
        self.ficha = ficha.strip().upper()

    def get_nombre(self):
        return self.nombre

    def get_ficha(self):
        return self.ficha 
        
    def __repr__(self):
        return f"Jugador(nombre='{self.nombre}', ficha='{self.ficha}')"
