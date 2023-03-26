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
