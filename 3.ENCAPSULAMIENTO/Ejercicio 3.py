# Clase Libro con atributos encapsulados (privados) y públicos
class Libro:
    # Método constructor
    def __init__(self, titulo, autor, isbn, editorial):
        self.__titulo = titulo  # Atributo privado
        self.__autor = autor    # Atributo privado
        self.__isbn = isbn      # Atributo privado
        self.editorial = editorial  # Atributo público

    # Método getter para titulo
    def obtener_titulo(self):
        return self.__titulo

    # Método getter para autor
    def obtener_autor(self):
        return self.__autor

    # Método getter para isbn
    def obtener_isbn(self):
        return self.__isbn

    # Método setter para titulo
    def establecer_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo

    # Método setter para autor
    def establecer_autor(self, nuevo_autor):
        self.__autor = nuevo_autor

    # Método setter para isbn
    def establecer_isbn(self, nuevo_isbn):
        self.__isbn = nuevo_isbn

    # Método para mostrar la información completa del libro
    def mostrar_info(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"ISBN: {self.__isbn}")
        print(f"Editorial: {self.editorial}")

# Crear objeto de la clase Libro
libro = Libro("El Quijote", "Miguel de Cervantes", "978-3-16-148410-0", "Editorial Clásica")

# Mostrar la información completa del libro
libro.mostrar_info()

print("\n----------------------------\n")

# Modificar los atributos privados usando los métodos setter
libro.establecer_titulo("Don Quijote de la Mancha")  # Setter
libro.establecer_autor("Cervantes")  # Setter
libro.establecer_isbn("123-4-56-789101-1")  # Setter

# Mostrar la información actualizada del libro
libro.mostrar_info()

# Obtener los valores individuales usando los métodos getter
print("\nTítulo actual: ", libro.obtener_titulo())  # Getter
print("Autor actual: ", libro.obtener_autor())  # Getter
print("ISBN actual: ", libro.obtener_isbn())  # Getter
