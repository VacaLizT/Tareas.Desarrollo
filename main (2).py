menu="""
    1. Comparación de tres números
    2. Relación entre dos números
    3. Evaluación de Expresiones Complejas
    4. Comprobar un año mágico
    5. Año Espejo
    6. Número balanceado de 4 dígitos
    7. Fecha con Propiedad Secreta.
   
"""
print(menu)
menu=input("Seleccione uno de los planteamientos: ")

if menu=="1":
    numero1=int(input("Ingrese el número 1: "))
    numero2=int(input("Ingrese el número 2: "))
    numero3=int(input("Ingrese el número 3: "))
    if (numero1==numero2==numero3):
        print("Los tres números son iguales.")
    elif (numero1==numero2):
        print("El número 1 y el 2 son iguales.")
    elif(numero1==numero3):
        print("El número 1 y el 3 son iguales.")
    elif(numero2==numero3):
        print("El número 2 y el 3 son iguales.")
    else:
        print("Todos los números son distintos.")
elif menu=="2":
    numero1=int(input("Ingrese el número 1: "))
    numero2=int(input("Ingrese el número 2: "))
    if (numero2*2==numero1):
        print("El número 1 es el doble del número 2.")
        if (numero1+numero2)%2!=0:
            print("La suma de los dos números es un número impar.")
        else:
            print("La suma de los dos números es un número par.")
    elif (numero1*2==numero2):
        print("El número 2 es el doble del número 1.")
        if (numero1+numero2)%2!=0:
            print("La suma de los dos números es un número impar.")
        else:
            print("La suma de los dos número es un número par.")
    else:
        print("Ninguno de los números es el doble del otro.")
        if (numero1+numero2)%2!=0:
            print("La suma de los dos números es un número impar.")
        else:
            print("La suma de los dos números es un número par.")
elif menu=="3":
    x=int(input("Ingrese el número 1: "))
    y=int(input("Ingrese el número 2: "))
    z=int(input("Ingrese el número 3: "))
    if (((x+y)*z)%(x-y))==0:
        print({(x+y)*z}," es múltiplo de: ", {x-y})
        if (x>y)and(x<z):
            print("El número" ,x, "es mayor que el número",y, "y menor que el número",z)
        else:
            print("El número" ,x, "no está entre el número",y,"y el número",z)
    else:
        print({(x+y)*z}," no es múltiplo de: ",{x-y})
        if (x>y)and(x<z):
            print("El número" ,x, "es mayor que el número" ,y,  "y menor que el número" ,z)
        else:
            print("El número" ,x,  "no está entre el número" ,y,  "y el número" ,z)
elif menu=="4":
    año=int(input("Ingrese el año: "))
    cifra1=año//100
    cifra2=año%100
    if (cifra1+cifra2==100):
        print("El año, es un año mágico.")
    else:
        print("El año, no es un año mágico.")
elif menu=="5":
    año=int(input("Ingrese el año: "))
    cifra1=año//1000
    cifra2=año%10
    cifra3=año%1000
    cifra4=cifra3//100
    cifra5=cifra3%100
    cifra6=cifra5//10
    if (cifra1==cifra2) and (cifra4==cifra6):
        print("El año, es un año espejo.")
    else:
        print("El año, no es un año espejo.")
elif menu=="6":
    numero=int(input("Ingrese un número de 4 cifras: "))
    cifra1=numero//1000
    cifra2=numero%10
    cifra3=numero%1000
    cifra4=cifra3//100
    cifra5=cifra3%100
    cifra6=cifra5//10
    if(cifra1+cifra2)==(cifra4+cifra6):
        print("El número es balanceado.")
    else:
        print("El número no es balanceado.")
elif menu=="7":
    dia=int(input("Ingrese el día: "))
    mes=int(input("Ingrese el mes: "))
    año=int(input("Ingrese el año: "))
    print(dia,"/",mes,"/",año)
    suma=dia+mes
    cifra1=año//100
    cifra2=año%100
    diferencia=cifra2-cifra1
    multiplicacion=(diferencia*suma)
    cuadraro=math.sqrt(multiplicacion)
    if cuadraro%0==true:
        print("La fecha es una fecha con propiedad secreta.")
    else:
        print("La fecha no tiene propiedad secreta.")