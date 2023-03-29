# Hacer un programa que calcule la suma, resta, multiplicación y división de dos números ingresados por el usuario.




# Hacer un programa que calcule el área y la circunferencia de un círculo.
radeo = 20
Pi = 3.14
Diametro = radeo*2
Circunferencia = Diametro * Pi
area = Pi * Diametro**2

print(f"El area del circulo es {area}")
print(f"La circunferencia es {Circunferencia}")

# Hacer un programa que calcule el promedio de una lista de números ingresados por el usuario.
numero = int(input("Por favor ingrese un numero: "))
numero_2 = int(input("Por favor ingrese un numero: "))
numero_3 = int(input("Por favor ingrese un numero: "))

promedio = numero + numero_2 + numero_3 / 3
print(f"El promedio de los numeros ingresados corresponde a {promedio}")



# Hacer un programa que determine si un número ingresado por el usuario es par o impar.
numero_del_usuario = int(input("Ingrese un número: "))

if numero_del_usuario % 2 == 0:
    print(numero_del_usuario, "es par.")
else:
    print(numero_del_usuario, "es impar.") 

# Hacer un programa que calcule la tabla de multiplicar de un número ingresado por el usuario.




# Hacer un programa que cuente la cantidad de letras y números en un texto ingresado por el usuario.
Letras = input("Pura vida, digame una palabra al azar señor: ")
contador_de_letras = len(Letras)
print(f"Pura vida pa la cantidad de letras de ese texto es {contador_de_letras}")


# Hacer un programa que ordene una lista de números ingresados por el usuario en orden ascendente o descendente.
num_de_usuario = int(input("Ingrese una cantidad de numeros al azar: "))
num_de_usuario(reverse = True)

print(num_de_usuario)