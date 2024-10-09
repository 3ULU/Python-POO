# Clase Producto con atributos encapsulados o privados
# Ejercicio 2: Clase Producto

class Producto:
    # Método constructor
    def __init__(self, nombre, precio, cantidad, categoria):
        self.__nombre = nombre  # privado
        self.__precio = precio  # privado
        self.cantidad = cantidad  # público
        self.categoria = categoria  # público

    # Método getter
    def obtener_nombre(self):
        return self.__nombre

    # Método setter
    def establecer_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    # Método getter
    def obtener_precio(self):
        return self.__precio

    # Método setter
    def establecer_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    # Método para mostrar toda la información del producto
    def mostrar_informacion(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Precio: {self.__precio}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Categoría: {self.categoria}")

# Crear un objeto de la clase Producto
producto = Producto("Laptop", 1200, 5, "Electrónica")

# Mostrar la información del producto
producto.mostrar_informacion()

print("----------------------------")

# Modificar los atributos privados usando los setters
producto.establecer_nombre("Laptop Gaming")
producto.establecer_precio(1500)

# Mostrar la información actualizada del producto
producto.mostrar_informacion()
