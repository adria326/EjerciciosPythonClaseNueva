#Escribi un programa que solicite al usuario dos numeros y los almacene
#en dos variables. En otra variable, almacena el resultadode la suma
#de esos dos numeros y luego mostrar ese resultado en pantalla.
#A continuacion, el programa debe solicitar al usuario que ingrese un
#tercer numero, elcual se debe alamcenar en una nueva variable.
#por ultimo,muestra es pantalla el resultado de la multiplicacion de
#este nuevo numero por el resultado de la suma anterior.

primerNumero = int(input("escribe el primer numero: "))
segundoNumero = int(input("escribe el segundo numero: "))

suma = primerNumero + segundoNumero
print(suma)

tercerNumero = int(input("escribe el tercer numero: "))
multiplicacion = tercerNumero * suma
print(multiplicacion)