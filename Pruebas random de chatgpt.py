# Le pedi a Chatgpt 3 que me diese un codigo al azar de al menos 2 variables
import random

# Generar una lista de números aleatorios
numeros = []
for i in range(10):
    numeros.append(random.randint(1, 100))

# Calcular el promedio de los números
total = 0
for numero in numeros:
    total += numero
promedio = total / len(numeros)

# Imprimir los resultados
print("La lista de números es:", numeros)
print("El promedio de los números es:", promedio)

# Programa para calcular el precio total de una compra
precio_unitario = 10.50
cantidad = 3
descuento = 0.20
envio = 5.00

subtotal = precio_unitario * cantidad
descuento_total = subtotal * descuento
envio_total = envio

total = subtotal - descuento_total + envio_total

print("El precio total de su compra es:", total)


edad = int(input("Digame su edad: "))

if edad >= 18:
    print("Eres Mayor de edad")
    print("Usted puede pasar")
else:
    print("No es mayor de edad")
    nombre_padre = input("Inserte el nombre de su padre/madre: ")
    id_padre = int(input("Inserte la identificación de su padre/madre: "))
    print(f"Gracias por la autorización, {nombre_padre} su hijo se le permite el ingreso")


numero_1 = int(input("Por favor ingresa un numero: "))
numero_2 = int(input("Por favor ingresa el segundo numero: "))
suma = numero_1 + numero_2
resta = numero_1 - numero_2
division = numero_1 / numero_2
multiplicacion = numero_1 * numero_2
opcion = 1 == suma
opcion = 2 == resta
3 == division
4 == multiplicacion
print(f"Bienvenido a la calculadora Por favor aprete {1} para suma {2} para resta {3} para division y {4} para multiplicacion")
int(input("Por favor digame su accion: "))
if opcion == 1:
    print(f"RESULTADO: La suma de {numero_1} + {numero_2}es igual a {suma}")
elif opcion == 2:
    print(f"RESULTADO: La resta de {numero_1} - {numero_2} es igual a {resta}")
