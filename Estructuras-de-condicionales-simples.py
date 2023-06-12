print("Estructura de-condicionales-simples")

#1 Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.
letra1= input("Introduzca por favor una letra")
letra2= input("Introduzca por favor otra letra")

if letra1 == letra2:
    print("Las dos letras son iguales")
else:
    print(F"Las dos letras ingresadas {letra1, letra2} son diferentes")

#2 Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.")

palabra1= input("Introduzca por favor una palabra")
palabra2= input("Introduzca por favor otra palabra para ser comparada")

if palabra1 == palabra2:
    print("Las dos palabras son iguales")
else:
    print(F"Las dos palabras ingresadas {palabra1, palabra2} son diferentes")

#3 Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.

genero= str(input("Introduzca f si es femenino:"))

if genero =="f":
    print("Usted vota en mesa femenina")
else:
    print("Usted vota en mesa masculina")

#4 Realice un programa que lea dos números y diga cuál es el mayor.

num1= float(input("Introduzca el primer numero:"))
num2= float(input("Introduzca el segundo numero:"))   

if num1>num2:
    print("El primer numero es mayor.")
else:
    print("El segundo numero es mayor.")

#5 Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa

print("Por favor, elija que operacion desea realizar.")
valordolar=480

while True:
    print("1. Cambiar pesos por dolares estadounidenses")
    print("2. Cambiar dolares estadounidenses a pesos")
    print("3. Salir")
    opcion = input("Seleccione una de las tres opciones (1, 2 o 3):")

    if opcion == "1":
        cantidadpesos= float(input("Ingrese la cantidad en pesos:"))
        conversionP_D= cantidadpesos/valordolar 
        print(f"{cantidadpesos} pesos equivale a {conversionP_D} dolares.")

    elif opcion == "2":
        cantidaddolar = float(input("Ingrese la cantidad en dolares:"))
        conversionD_P= cantidadpesos*cantidaddolar
        print(f"{cantidaddolar} dolares equivale a {conversionD_P} pesos.")

    elif opcion=="3":
        print("Estimado cliente, gracias por utilizar nuestro servicio.")
        break
        
    else:
        print("Opcion invalida. Por favor,seleccione una opcion valida.")
        continue

#6 Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.

edad= int(input("Introduzca su edad:"))

if edad>16:
    print("Usted puede votar")

elif edad<18:
    print("Usted es menor de edad, por ende no puede votar")

else:
    print("La opcion ingresada no es correcta")
