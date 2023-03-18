# Esto va a ser parte de la investagacion sobre input 

Usuario = input(f"Su nombre de usuario es: ")
print(f"Bienvenido {Usuario} ")



# Ejercicio 1 "Con razon se llamaba "de investigacion" fue algo tardado encontrar que existian los .lower .upper"
print("------------------------------")
nombre_completo = input("Porfavor escriba su nombre completo: ")

print(nombre_completo.lower())

print(nombre_completo.upper())

print(nombre_completo.title())

# Ejercicio 2 Esto fue una tortura de sacar, especificamente porque todo el rato me sacaba de resultado el nombre tipo "LuisLuisLuis" En vez de un salto de linea de codigo
# Imagina mi cara cuando me di cuenta del \n
print("------------------------------")
Administrador = input(f"Bienvendido: ")
Repeticion = int(input("Por favor ingresa un numero: "))


print("Me gusta tu nombre \n" + (Administrador + "\n") * Repeticion)



# Ejercicio 3 "Cosa curiosa, me confundi y como por 1 hora estuve intentando usar el "count" sin tener idea de que el "len" era lo que necesitaba exactamente"
Tu_nombre = input("Pura vida, digame su nombre señor: ")
numero_de_letras = len(Tu_nombre)
print(f"Bienvenido {Tu_nombre.upper()} el numero de letras de tu nombre es {numero_de_letras}")