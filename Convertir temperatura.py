
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convertir_temperatura():
    print("¿Qué conversión desea realizar?")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = int(input("Ingrese una opción: "))
    temperatura = float(input("Ingrese la temperatura: "))
    if opcion == 1:
        resultado = celsius_a_fahrenheit(temperatura)
        print(f"{temperatura} grados Celsius son {resultado} grados Fahrenheit.")
    elif opcion == 2:
        resultado = fahrenheit_a_celsius(temperatura)
        print(f"{temperatura} grados Fahrenheit son {resultado} grados Celsius.")
    else:
        print("Opción inválida.")

convertir_temperatura()
