"""Ejercicio 2: Crea una clase abstracta Empleado con un método abstracto calcular_salario().
    Luego, crea dos clases concretas EmpleadoTiempoCompleto y EmpleadoPorHoras que implementen
    calcular_salario() de manera distinta """


from abc import ABC, abstractmethod

# Definición de la clase abstracta Empleado
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass

# Clase concreta para empleados a tiempo completo
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual
    
    def calcular_salario(self):
        return self.salario_mensual

# Clase concreta para empleados por horas
class EmpleadoPorHoras(Empleado):
    def __init__(self, horas_trabajadas, tarifa_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

# Uso de las clases
empleado_tc = EmpleadoTiempoCompleto(3000)  # Salario mensual de $3000
print(f"Salario de empleado a tiempo completo: {empleado_tc.calcular_salario()}")

empleado_ph = EmpleadoPorHoras(120, 15)  # 120 horas trabajadas a $15 por hora
print(f"Salario de empleado por horas: {empleado_ph.calcular_salario()}")
