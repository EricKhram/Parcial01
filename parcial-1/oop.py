#AI-TRAP:OOP
# Este ejercicio representa el modelado de personas y empleados, útil en sistemas de gestión de recursos humanos o nómina.

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def es_mayor(self):
        if self.edad >= 18:
            return 'si'
        return 'no'

class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

class main():
    empleadoej = Empleado("Erick Lopez",17,1500000)
    print (f"el empleado {empleadoej.nombre} tiene un sueldo de {empleadoej.salario} y ¿es mayor de edad?: {empleadoej.es_mayor()}")

if __name__ == "__main__":
    main()
