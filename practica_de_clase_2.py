# Esto va a ser parte de la investagacion sobre input 

Usuario = input(f"Su nombre de usuario es: ")
print(f"Bienvenido {Usuario} ")



# Parte 2 "Con razon se llamaba "de investigacion" fue algo tardado encontrar que existian los .lower .upper"
print("------------------------------")
nombre_completo = input("Porfavor escriba su nombre completo: ")

print(nombre_completo.lower())

print(nombre_completo.upper())

print(nombre_completo.title())

# Parte 3 Esto fue una tortura de sacar, especificamente porque todo el rato me sacaba de resultado el nombre tipo "LuisLuisLuis" En vez de un salto de linea de codigo
print("------------------------------")
Administrador = input(f"Bienvendido: ")
Repeticion = int(input("Por favor ingresa un numero: "))


print("me gusta tu nombre \n" + (Administrador + "\n") * Repeticion)
