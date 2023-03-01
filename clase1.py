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

