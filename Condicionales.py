"""a = int(input("Ingresa un numero: "))
if a == 0:
    print("El numero es cero")
else:
    if a > 0:
        if a % 2 == 0:
            print("El numero es par y positivo")
        else:
            print("El numero es impar y positivo")
    else:
        if a % 2 == 0:
            print("El numero es par y negativo")
        else:
            print("El numero es impar y negativo")"""

edad = int(input("Ingresa tu edad: "))
print("Eres mayor de edad: ") if edad >= 18 else print("Eres menor de edad")