multiplos=[]
contador=0
num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
for i in range (num1):
    contador+=1
    multiplicaion=(contador*num2)
    multiplos.append(multiplicaion)
print(multiplos)


nombres=[]
longitud=[]
contador=0
numero=int(input("Ingrese la cantidad de nombres que desea ingresar: "))

for i in range(numero):
    contador=0
    nombre=input("Ingrese el nombre: ")
    nombres.append(nombre)
    for i in nombre:
        contador+=1
    longitud.append(contador)
print(nombres)
print(longitud)