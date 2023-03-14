# Son 4 tipos de variable
# string 
print ("Mae")
name ="Pura vida mae"
last_name = "Que me dice"

# Integer
id = 4119200511

# float 
cash = 4,6

# Bool
male = True 

# Comparaciones de las variables

# Como verificar si el PIN ingresado por un usuario coincide con su PIN guardado

entered_pin = 1234
expected_pin = 1234

result = entered_pin == expected_pin

print (result)

# Comparaciones con desigualgad. Tenemos que usar el operador !=

result_1 = 1 !=2
print(result_1)

one = 1
two = 2
print("----------------------")
print  (one == two)
print (one != two)


# Vamos a hacer que un interruptor de luz inteligente que apague las luces si es de dia y las encienda si es de noche
print("----------------------")
is_day= True
lights_on= not is_day

print("Daytime?")
print(is_day)

print("lights_on?")
print(lights_on)

# Con las comparaciones vamos a hacer un codigo que rastree los datos de ventas de una tienda de pantalones
print("-----------------")

stock = 600
jeans_sold = 500
target = 500

target_hit = jeans_sold == target
print ("hit jeans sale target:")
print (target)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print ("Jeans in Stock: ")
print(in_stock)
print(current_stock)


# Podemos usar comparaciones para verificas si un numero es mayor o menor que otro numero

print("-----------------------------")

print(2 < 200)
print(2 > 200)

print(201 <= 200)
print(2 >= 200)

print("-----------------------")

# Comparaciones de cadenas de texto

my_answer = "lowr"
solution = "low"

print(my_answer == solution)
print(my_answer != solution)

# Ejercisio de medidor de frecuencia cardiaca usando comparaciones para verificar si la frecuencia cardiaca es demasiado baja o alta y le diermos al paciente si debe preocuparse
print("----------------------------------")

Pulso = 100
Salud = "sano"
Peligro = "Esta con dios"


print (Pulso == Salud) 
print(Salud)
print (Pulso != Salud)
print(Peligro)

# Como lo hizo el profe
print("----------------------------")
heart_rate= 177

too_low = heart_rate < 60
too_high = heart_rate > 100

print ("Heart rate high?")
print (too_low)

print("Heart right high?")
print (too_high)

# Practica
print("---------------------------------------")
numero1 = 5
numero2= 5
resultado = numero2 + numero1
print(resultado)

# Practica de edad
print("----------------------------------")
edad = 18
Esmayor = edad>=18
print ("Es mayor de edad?")
print(Esmayor)

# Usemos comparaciones de string para etiquietar los datos adquiridos a traves de la encuesta de usuarios de una aplicacion de fitness.
# Verificamos las respuestas de la encuesta de los usuarios con respecto a la frecuencia e instensidad de la actividad, las etiquetaremos y mostraremos los resultados.

print("-----------------------------------------")

frecuencia = "Una vez a la semana"
intensidad = "alta"

activo = frecuencia == "Diaria"
print ("El usuario es activo?")
print (activo)

intenso = intensidad == "alta"
print ("El usuario es intenso?")
print (intenso)

print (f"La edad de Luis Diego es: {edad} y su apellido es Picado, la intensidad de su ejercisio es {intensidad} y su frecuencia es {frecuencia}") 

# El profe puso de practica
print("--------------------------------------------------------------------------")

Numero_de_celular = "85631331"

respuesta_si =  f"https://wa.me/506{Numero_de_celular}"


print("si quieres tener exito")
print(f"Este es tu Link {respuesta_si}")

