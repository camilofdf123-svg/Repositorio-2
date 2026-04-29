nombre, edad, puntaje, asistencia, codigo_invitacion = input("Ingresa tu nombre: "), int(input("Ingresa tu edad: ")), float(input("Ingresa tu puntaje: ")), int(input("Ingresa tu asistencia: ")), input("Ingresa tu codigo de invitacion: ")
nombre.replace(" ", "")
print("Participante: ", nombre.upper())
print("Caracteres en el nombre: ", len(nombre))
promedio = (puntaje + asistencia) / 2
print("Promedio general: ", promedio)
if edad >= 14:
    if promedio >= 80:
        if codigo_invitacion == "PYTHON2026":
            print("Resultado: Acceso VIP")
        else:
            print("Resultado: Acceso general")
    else:
        if promedio <= 60:
            print("Resultado: No puede ingresar por bajo rendimiento")
else:
    if codigo_invitacion == "PYTHON2026":
        print("Resultado: Acceso especial con acompañante") 
    else:
        print("Resultado: No cumple edad minima")
if puntaje >= 90 and asistencia >= 90:
    print("Mensaje adicional: Candidato destacado")
if puntaje < 50 or asistencia < 50:
    print("Mensaje adicional: Requiere refuerzo previo")