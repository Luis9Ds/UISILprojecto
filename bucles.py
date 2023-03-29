# While y For
# Un bucle while repite su bucl de codigo mientras su condiciones true 

# Para detener el bucle creamos una variable antes de crear el bucle
control = True


while control == True:
    print("Hola Mundo")

    control = False

    print("Se mostro 1 vez")

# Para controlar las veces que se repite un bucle while comenzamos con una variable establecida en un numero, Llamamos a esta variable contador.

Contador = 1
controlador = True
Contador_Fix = Contador - 10
while Contador < 10:
    print (Contador)
    Contador += 1 

# Calculo de interes compuesto

cuenta = 100
interes= 0.11
annos = 9

print("Monto inicial:", cuenta)

contador = 1
while contador <= annos:
    interes_compuesto = cuenta * interes
    cuenta += interes_compuesto
    cuenta += 100
    print("Año", contador, ": ",cuenta)
    contador += 1


