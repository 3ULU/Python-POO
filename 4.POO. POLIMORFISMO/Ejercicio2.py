# Clase Carro
class Carro:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def descripcion(self):
        print("Vehículo de tipo Carro")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print("-------------------------")
        
# Clase Moto
class Moto:
    def __init__(self, marca, modelo, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
    
    def descripcion(self):
        print("Vehículo de tipo Moto")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Cilindrada: {self.cilindrada} cc")
        print("-------------------------")
        
# Clase Bicicleta
class Bicicleta:
    def __init__(self, marca, tipo, cambios):
        self.marca = marca
        self.tipo = tipo
        self.cambios = cambios
    
    def descripcion(self):
        print("Vehículo de tipo Bicicleta")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Número de cambios: {self.cambios}")
# Función que muestra la descripción de cualquier tipo de vehículo
def mostrar_descripcion(vehiculo):
    vehiculo.descripcion()

# Instancias de cada clase
vehiculo_carro = Carro("Toyota", "Corolla", 2020)
vehiculo_moto = Moto("Yamaha", "R3", 321)
vehiculo_bicicleta = Bicicleta("Trek", "Montaña", 21)

# Llamado al método descripcion() para cada objeto
mostrar_descripcion(vehiculo_carro)
mostrar_descripcion(vehiculo_moto)
mostrar_descripcion(vehiculo_bicicleta)
