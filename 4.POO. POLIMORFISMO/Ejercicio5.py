# Clase Médico
class Medico:
    def __init__(self, nombre, especialidad, años_experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.años_experiencia = años_experiencia
    
    def trabajar(self):
        print("Profesión: Médico")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Años de experiencia: {self.años_experiencia}")
        print("--------------------------------------------")
# Clase Ingeniero
class Ingeniero:
    def __init__(self, nombre, rama, proyectos_completados):
        self.nombre = nombre
        self.rama = rama  # Ej: civil, software, mecánico
        self.proyectos_completados = proyectos_completados
    
    def trabajar(self):
        print("Profesión: Ingeniero")
        print(f"Nombre: {self.nombre}")
        print(f"Rama: {self.rama}")
        print(f"Proyectos completados: {self.proyectos_completados}")
        print("--------------------------------------------")
# Clase Docente
class Docente:
    def __init__(self, nombre, asignatura, nivel_educativo):
        self.nombre = nombre
        self.asignatura = asignatura
        self.nivel_educativo = nivel_educativo  # Ej: primaria, secundaria, universidad
    
    def trabajar(self):
        print("Profesión: Docente")
        print(f"Nombre: {self.nombre}")
        print(f"Asignatura: {self.asignatura}")
        print(f"Nivel educativo: {self.nivel_educativo}")
        print("--------------------------------------------")
# Función que muestra la información técnica de cualquier tipo de profesional
def mostrar_informacion_profesional(profesional):
    profesional.trabajar()

# Instancias de cada clase
profesional_medico = Medico("Ana Gómez", "Cardiología", 10)
profesional_ingeniero = Ingeniero("Carlos Pérez", "Software", 25)
profesional_docente = Docente("María Rodríguez", "Matemáticas", "Universidad")

# Llamado al método trabajar() para cada objeto
mostrar_informacion_profesional(profesional_medico)
mostrar_informacion_profesional(profesional_ingeniero)
mostrar_informacion_profesional(profesional_docente)
