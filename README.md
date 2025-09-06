# Parcial 1 – Paradigmas de Programación - Erick Lopez

## Errores encontrados en el primer ejercicio (Estructurado)

### Primer error
En el else de la estructura condicional faltaba un : que indica que va a ejectar el mismo

### Segundo error  
en el ejercio se pide que este debe sumar ventas o reportes pero como tal no le estamos pasando ninguna lista
por lo que procederemos en el main a crearla 
asi como tambien a llamar a la funcion suma_lista y ingresandole la lista de ventas que creamos para que luego el print nos muestre si es mayor o menor que 100

```python
def main():
    ventas = [10,30,20,5]
    resultado = suma_lista(ventas)
    print(f"la suma de las ventas {ventas} es {resultado} que 100")
```


### Tercer Error
por ultimo no se estaba llamando a la funcion que haciamos por lo cual no podiamos comprobar el funcionamiento del programa por lo cual lo agregamos
aunque igual el programa lo verificamos atravez del debugging

```python
if __name__ == "__main__":
    main()
```



## Errores encontrados en el segundo ejercicio (POO)

### Primer error
en la clase del empleado no estabamos llamando el constructor de persona (el que hereda empleado), por lo cual no podriamos usar el nombre y edad de la persona en la clase empleado
esto lo podemos solucionar con super() de la siguiente manera 

```python
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario
```

para que asi lo herede correctamente

### Segundo error o complemento
como complemento para el ejercicio crearia un main donde le pase los 3 datos de un empleado para verificar que si se este heredando correctamente los atributos y las funciones de la clase persona

```python
class main():
    empleadoej = Empleado("Erick Lopez",17,1500000)
    print (f"el empleado {empleadoej.nombre} tiene un sueldo de {empleadoej.salario} y ¿es mayor de edad?: {empleadoej.es_mayor()}")
```

y luego lo ejecuto para verificar

```python
if __name__ == "__main__":
    main()
```

ademas de hacer el debugging para verficar el paso a paso del programa