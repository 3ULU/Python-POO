"""Ejercicio 3: Crea una clase abstracta TareaEmpleado con un método abstracto realizar_tarea().
Implementa las clases Ingeniero y Doctor que heredan de TareaEmpleado e implementan el método realizar_tarea()
de manera específica según su especialidad."""
from abc import ABC, abstractmethod

# Definición de la clase abstracta TareaEmpleado
class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

# Clase concreta para Ingenieros
class Ingeniero(TareaEmpleado):
    def __init__(self, nombre):
        self.nombre = nombre

    def realizar_tarea(self):
        return f"{self.nombre} está diseñando un sistema de software."

# Clase concreta para Doctores
class Doctor(TareaEmpleado):
    def __init__(self, nombre):
        self.nombre = nombre

    def realizar_tarea(self):
        return f"{self.nombre} está atendiendo a un paciente."

# Uso de las clases
ingeniero = Ingeniero("Luis")
print(ingeniero.realizar_tarea())

doctor = Doctor("Ana")
print(doctor.realizar_tarea())
