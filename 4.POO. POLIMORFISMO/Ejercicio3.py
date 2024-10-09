# Clase Perro
class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    def sonido(self):
        print(f"{self.nombre}, un perro de raza {self.raza}, hace: Guau guau")

# Clase Gato
class Gato:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    
    def sonido(self):
        print(f"{self.nombre}, un gato de color {self.color}, hace: Miau miau")

# Clase Pájaro
class Pajaro:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    
    def sonido(self):
        print(f"{self.nombre}, un pájaro de especie {self.especie}, hace: Pío pío")

# Función que muestra el sonido de cualquier tipo de animal
def mostrar_sonido(animal):
    animal.sonido()

# Instancias de cada clase
animal_perro = Perro("Zeus", "Labrador")
animal_gato = Gato("chumuelo", "Negro")
animal_pajaro = Pajaro("Piolín", "Canario")

# Llamado al método sonido() para cada objeto
mostrar_sonido(animal_perro)
mostrar_sonido(animal_gato)
mostrar_sonido(animal_pajaro)
