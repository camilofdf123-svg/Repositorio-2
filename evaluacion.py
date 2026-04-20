# ===== PARTE A =====
# 1. Análisis de datos y código
# a) nombre (str), edad (int), promedio (float), cursos (list)
# b) Se monstraria el tipo de dato y el len del nombre: str, int, float, list, 5
# c) El len cuenta el número de letras en el string. En este caso, "Lucía" tiene 5

# 2. Comprensión conceptual
# a) ¿Qué diferencia hay entre print() e input()? print muestra el resultado de una operación o un mensaje, mientras que input pide al usuario ingresar datos.
# b) ¿Por qué un dato ingresado con input() puede dar error si se usa directamente en un cálculo?
# Porque input() funciona con string, y si se intenta usar en un cálculo sin convertir a números con int() o float(), da un error.
# c) Explica la diferencia entre /, // y %. / es division normal, // es división entera y % es el operador de módulo.
# d) Escribe una instrucción que permita comprobar la versión de Python que se está usando. sys.version 
# e) Escribe una instrucción que permita consultar las palabras reservadas de Python. keyword.kwlist

# ===== PARTE B =====
# 3. Corrección de código
"""ancho = input("Ingrese el ancho del terreno: ")
largo = input("Ingrese el largo del terreno: ")
precio = input("Ingrese el precio por metro cuadrado: ")
area = ancho * largo
costo = area * precio
print("Área total: " + area)
print("Costo estimado: " + costo)"""

#Correcion:

ancho = float(input("Ingrese el ancho del terreno: "))
largo = float(input("Ingrese el largo del terreno: "))
precio = float(input("Ingrese el precio por metro cuadrado: "))
area = ancho * largo
costo = area * precio
print("Área total: ", str(area))
print("Costo estimado: ", str(costo))

# a) ¿Cuáles eran los errores principales? Los errores principales eran que las variables estaban como strings. Además, cuando se hizo print del el área y el costo, se intentaba unir un string con un número. 
# b) ¿Por qué tu corrección sí permite obtener resultados válidos? Porque el input se convirtió a números con float() para calculos, y se uso str() para convertir los resultados a strings al hacer print.

#4. Construcción breve
TecnologíaParaTodos = "Tecnología para todos"
print(TecnologíaParaTodos.upper())
print(len(TecnologíaParaTodos))
print("Python" in TecnologíaParaTodos)
print(TecnologíaParaTodos.replace("Tecnología", "Python"))
print(TecnologíaParaTodos.split())

# ===== PARTE C =====
#5. Desarrolla un programa
Nombre, apellido, país, ancho, alto, metro = input("¿Cuál es tu nombre?"), input("¿Cuál es tu apellido?"), input("¿Cuál es tu país?"), float(input("¿Cuál es el ancho de tu terreno?")), float(input("¿Cuál es el alto de tu terreno?")), float(input("¿Cuál es el precio por metro cuadrado? "))
area = ancho * alto
costo = area * metro
NombreCompleto = Nombre + " " + apellido
print("Nombre: {}, Localizacion: {}. El area total es {} m² y el costo estimado es ${}".format(NombreCompleto, país, area, costo))
print(NombreCompleto.upper())
print(len(NombreCompleto))
print("a" in NombreCompleto)
print(costo > 100)