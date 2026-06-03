"""def obtener_mensaje():
    mensaje = 'Bienvenido al sistema'
    return mensaje

def generar_nombre_completo():
    nombre = 'Santiago'
    apellido = 'Moreno'
    espacio = ' '
    nombre_completo = nombre + espacio + apellido
    return nombre_completo

print(obtener_mensaje())
print(generar_nombre_completo())"""

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir para cero."
while True:
    print("CALCULADORA BÁSICA")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Seleccione una operación (1-5): ")

    if opcion == "5":
        print("Programa finalizado.")
        break

    if opcion = "1" or opcion = "2" or opcion = "3" or opcion = "4":
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))

        if opcion == "1":
            print("Resultado:", suma(num1, num2))
        elif opcion == "2":
            print("Resultado:", resta(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicacion(num1, num2))
        elif opcion == "4":
            print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida. Intente nuevamente.")
