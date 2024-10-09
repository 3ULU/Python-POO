# Clase Guitarra
class Guitarra:
    def __init__(self, marca, tipo, cuerdas):
        self.marca = marca
        self.tipo = tipo  # Puede ser acústica, eléctrica, etc.
        self.cuerdas = cuerdas
    
    def tocar(self):
        print("Instrumento: Guitarra")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Número de cuerdas: {self.cuerdas}")
        print("-------------------------------------")
# Clase Piano
class Piano:
    def __init__(self, marca, tipo, teclas):
        self.marca = marca
        self.tipo = tipo  # Puede ser de cola, vertical, eléctrico, etc.
        self.teclas = teclas
    
    def tocar(self):
        print("Instrumento: Piano")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Número de teclas: {self.teclas}")
        print("-------------------------------------")
# Clase Trompeta
class Trompeta:
    def __init__(self, marca, material):
        self.marca = marca
        self.material = material  # Ej: latón, acero
    
    def tocar(self):
        print("Instrumento: Trompeta")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print("-------------------------------------")
# Función que muestra la información técnica de cualquier tipo de instrumento
def mostrar_informacion_instrumento(instrumento):
    instrumento.tocar()

# Instancias de cada clase
instrumento_guitarra = Guitarra("Fender", "Eléctrica", 6)
instrumento_piano = Piano("Yamaha", "De cola", 88)
instrumento_trompeta = Trompeta("Bach", "Latón")

# Llamado al método tocar() para cada objeto
mostrar_informacion_instrumento(instrumento_guitarra)
mostrar_informacion_instrumento(instrumento_piano)
mostrar_informacion_instrumento(instrumento_trompeta)
