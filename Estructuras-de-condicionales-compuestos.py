print("Estructuras condicional compuesto")

#1 Introducir los lados de un triángulo y visualizar por pantalla si dicho #triángulo es equilátero, isósceles o escaleno.

ladoa=int(input("Introduzca la medida del lado A:"))
ladob=int(input("Introduzca la medida del lado B:"))
ladoc=int(input("Introduzca la medida del lado C:"))

if ladoa == ladob == ladoc:
    print("El triángulo es equilátero.")
elif ladoa != ladob != ladoc != ladoa:
    print("El triángulo es escaleno.")
else:
    print("El triángulo es isósceles.")

#2 Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:

while True:
    print("Seleccione que medio de pago desea utilizar.")
    print("1. Efectivo")
    print("2. Tarjeta de Credito")
    print("3. Tarjeta de Debito")
    print("4. Salir ")
    opcion = input("Seleccione alguna de las opciones.")
    monto=any

    if opcion=="1":
        print("El pago en efectivo tiene descuento del 10% en este local.")
        descuento= 0.1*monto
        print(F"El monto a pagar es {monto-descuento} y el descuento es de {descuento}")
        print("Gracias por su compra.")
        break
    elif opcion=="2":
        print("El pago con tarjeta de credito tiene un recargo del 10% en este local.")
        recargo=monto*0.1
        print(F"El monto a pagar es {monto+recargo} y el recargo es del {recargo}")
        print("Gracias por su compra.")
        break
    elif opcion=="3":
         print("El pago con tarjeta de debito tiene descuento del 5% en este local.")
         descuento= 0.05*monto
         print(F"El monto a pagar es {monto-descuento} y el descuento es de {descuento}")
         print("Gracias por su compra.")
         break
    elif opcion=="4":
        print("Sesion finalizada")
        break
    else:
        print("La opcion ingresada no es correcta.")
        continue
    
#3 Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.

num1 = int(input("Introduzca el primer número:"))
num2 = int(input("Introduzca el segundo número:"))
num3 = int(input("Introduzca el tercer número:"))
num = any

if num1 >= num2 and num1 >= num3:
    mayor = num1
elif num2 >= num1 and num2 >= num3:
    mayor = num2
else:
    mayor = num

print("El numero mayor es:", mayor)

if mayor % 2 == 0:
   print("El numero mayor es par.")
else:
    print("El numero mayor es impar.")

#4 Confeccione un programa que pida un número del 1 al 7 y diga el día de #la semana correspondiente.

num = int(input("Introduzca un número del 1 al 7:"))

if num == 1:
    print("El número", num, "es el día lunes.")
elif num == 2:
    print("El número", num, "es el día martes.")
elif num == 3:
    print("El número", num, "es el día miercoles.")
elif num == 4:
    print("El número", num, "es el día jueves.")
elif num == 5:
    print("El número", num, "es el día viernes.")
elif num == 6:
    print("El número", num, "es el dia sabado.")
elif num == 7:
    print("El número", num, "es el dia domingo.")
else:
    print("Número no válido. Introduzca un número del 1 al 7.")
 
#5 Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.

num = int(input("Introduzca un número del 1 al 12: "))

if num == 1:
    print("El número", num, "corresponde a enero.")
elif num == 2:
    print("El número", num, "corresponde a febrero.")
elif num == 3:
    print("El número", num, "corresponde a marzo.")
elif num == 4:
    print("El número", num, "corresponde a abril.")
elif num == 5:
    print("El número", num, "corresponde a mayo.")
elif num == 6:
    print("El número", num, "corresponde a junio.")
elif num == 7:
    print("El número", num, "corresponde a julio.")
elif num == 8:
    print("El número", num, "corresponde a agosto.")
elif num == 9:
    print("El número", num, "corresponde a septiembre.")
elif num == 10:
    print("El número", num, "corresponde a octubre.")
elif num == 11:
    print("El número", num, "corresponde a noviembre.")
elif num == 12:
    print("El número", num, "corresponde a diciembre.")
else:
    print("Número invalido. Por favor, introduzca un número del 1 al 12.")    