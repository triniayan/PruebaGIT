print("Estructuras repetitivas y condicionales")

#1 Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.

while True:
    pares = 0
    suma_pares = 0

    for i in range(1, 5):
        numero = int(input(f"Introduzca el numero {i} de 4:"))

        if numero % 2 == 0:
            pares += 1
            suma_pares += numero

    impares = 4 - pares

    print("Cantidad de numeros pares:", pares)
    print("Cantidad de numeros impares:", impares)
    print("Suma de numeros pares:", suma_pares)

#2 Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número máximo y cuál es el número mínimo.

while True:
    numeros = []

    for i in range(10):
        numero = float(input("Introduzca un numero:"))
        numeros.append(numero)

    print("Numeros introducidos:", numeros)

    mayores_100 = 0
    menores_100 = 0
    maximo = max(numeros)
    minimo = min(numeros)

    for numero in numeros:
        if numero > 100:
            mayores_100 += 1
        else:
            menores_100 += 1

    print("Cantidad de numeros mayores a 100:", mayores_100)
    print("Cantidad de numeros menores a 100:", menores_100)
    print("Numero maximo:", maximo)
    print("Numero minimo:", minimo)

#3 Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayores de edad y cuántos menores de edad.

contador_mujeres = 0
contador_varones = 0
contador_mayores = 0
contador_menores = 0

for i in range(15):
    edad = int(input("Introduzca la edad {}:".format(i + 1)))
    sexo = input("Introduzca el sexo {}):".format(i + 1))

    if sexo == "femenino" or sexo=="mujer":
        contador_mujeres += 1
    elif sexo == "masculino" or sexo=="varon":
        contador_varones += 1

    if edad >= 18:
        contador_mayores += 1
    else:
        contador_menores += 1

print("Cantidad de mujeres:", contador_mujeres)
print("Cantidad de varones:", contador_varones)
print("Cantidad de mayores de edad:", contador_mayores)
print("Cantidad de menores de edad:", contador_menores)

#4 Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

suma_positivos = 0

for i in range(10):
    numero = float(input("Introduzca un numero:"))
    if numero > 0:
        suma_positivos += numero
    elif numero<0:
        print("El numero introducido es negativo.")

print("La suma de los numeros positivos es:", suma_positivos)

#5 Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

for i in range(15):
    numero = float(input("Introduzca un numero negativo:"))    
    if numero < 0:
        numero = abs(numero)
        
        print("Numero convertido a positivo es: ", numero)
    else:
        print("El numero introducido no es negativo.")
