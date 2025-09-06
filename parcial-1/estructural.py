#AI-TRAP:ESTRUCTURAL
# Este ejercicio simula el procesamiento de una lista de datos, como sumar ventas diarias o calcular totales en reportes financieros.

def suma_lista(lista):
    resultado = 0
    for i in lista:
        resultado = resultado + i
    if resultado > 100:
        return 'mayor'
    else:
        return 'menor' 

def main():
    ventas = [10,30,20,5]
    resultado = suma_lista(ventas)
    print(f"la suma de las ventas {ventas} es {resultado} que 100")

if __name__ == "__main__":
    main()

