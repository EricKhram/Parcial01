# Parcial 1 – Paradigmas de Programación - Erick Lopez

## Errores encontrados en el primer ejercicio (Estructurado)

### primero
En el else de la estructura condicional faltaba un : que indica que va a ejectar el mismo

### segundo  
en el ejercio se pide que este debe sumar ventas o reportes pero como tal no le estamos pasando ninguna lista
por lo que procederemos en el main a crearla 
asi como tambien a llamar a la funcion suma_lista y ingresandole la lista de ventas que luego con el print nos muestre si es mayor o menor que 100

```python
def main():
    ventas = [10,30,20,5]
    resultado = suma_lista(ventas)
    print(f"la suma de las ventas {ventas} es {resultado} que 100")
```


### tercero
por ultimo no se estaba llamando a la funcion que haciamos por lo cual no podiamos comprobar el funcionamiento del programa

## Instrucciones Generales

- El parcial consta de ejercicios de los paradigmas estructural y orientado a objetos.
- Cada ejercicio contiene errores de lógica y/o sintaxis.
- El estudiante debe identificar y corregir los errores.
- Justifique cada cambio realizado.
- No utilice herramientas automáticas de IA.
- Tiempo máximo: 2 horas.
- Valor total: 5.0 puntos.