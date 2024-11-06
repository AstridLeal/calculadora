import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Sumar una lista de números")

while True:
    mostrar_menu()
    opcion = input("Ingresa una opción (1/2/3/4/5): ")

    if opcion == '1':
        a, b = float(input("Ingresa el primer número: ")), float(input("Ingresa el segundo número: "))
        print("Resultado:", sumar.sumar(a, b))
    elif opcion == '2':
        a, b = float(input("Ingresa el primer número: ")), float(input("Ingresa el segundo número: "))
        print("Resultado:", resta.restar(a, b))
    elif opcion == '3':
        a, b = float(input("Ingresa el primer número: ")), float(input("Ingresa el segundo número: "))
        print("Resultado:", multiplicacion.multiplicar(a, b))
    elif opcion == '4':
        a, b = float(input("Ingresa el primer número: ")), float(input("Ingresa el segundo número: "))
        print("Resultado:", dividir.dividir(a, b))
    elif opcion == '5':
        numeros = list(map(float, input("Ingresa una lista de números separados por espacio: ").split()))
        print("Resultado:", suma_avanzada.suma_avanzada(numeros))
    else:
        print("Opción no válida")
