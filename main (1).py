numero=int(input("Ingrese un número: "))
suma=0
n=1
while n<=numero:
    suma=suma+n
    n=n+1
print("La suma de los números es",suma)



numero=int(input("Ingrese un número: "))
multiplicacion=1
n=1
while n<=numero:
    multiplicacion=multiplicacion*n
    n=n+1
print("El factorial de los números es: ",multiplicacion)



num=34
variable=int(input("Adivine un número de 1 al 100. Ingrese el número que cree que es: "))
while variable!=num:
    if (variable<0) or ( variable>100):
        print("Número incorrecto.")
        variable=int(input("Intentelo de nuevo: "))
    if (variable<0) or ( variable>100):
        print("Número incorrecto.")
        variable=int(input("Intentelo de nuevo: "))  
    elif variable<num:
        print("El número es mayor.")
        variable=int(input("Intentelo de nuevo: "))    
    elif variable>num:
        print("El número es menor.")
        variable=int(input("Intentelo de nuevo: "))
if variable==num:
    print("Felicidades respuesta correcta")
    
    
    
contraseña=147258369
ingresar=int(input("Ingrese la contraseña: "))
while ingresar!=contraseña:
    if ingresar!=contraseña:    
        print("Contraseña incorrecta.")
        ingresar=int(input("Intentelo de nuevo: "))
    elif ingresar!=contraseña:
        print("Contraseña incorrecta.")
        ingresar=int(input("Intentelo de nuevo: "))
        break
    elif ingresar!=contraseña:
        print("Contraseña incorrecta, su cuenta sera bloqueada por los próximos 36 años. '_' .")
        break
if contraseña==ingresar:
    print("Contraseña correcta. :)")