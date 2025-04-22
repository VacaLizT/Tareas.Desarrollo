n=int(input("Ingrese la cantidad de clientes: "))
p=n
lista=[]
promedio=0
uno, dos, tres, cuatro, cinco=0,0,0,0,0
suma=0
while n!=0:
    nota=int(input("Ingrese la calificación: "))
    lista.append(nota)
    suma=suma+nota
    n=n-1
    if nota ==1:
        uno+=1
    elif nota==2:
        dos+=1
    elif nota==3:
        tres+=1
    elif nota==4:
        cuatro+=1
    elif nota==5:
        cinco+=1
print(f"Malo: {uno}, Regular: {dos}, Bueno: {tres}, Muy bueno: {cuatro}, Excelente: {cinco}")
prom=suma/p
print(f"El promedio es: {prom}")
for i in lista:
    if i <prom:
        promedio=promedio+1
print((promedio*100/p), "% está debajo del promedio")

