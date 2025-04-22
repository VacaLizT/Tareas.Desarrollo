print("Vamos a convertir un número Octal a un número Hexadecimal.")
n=int(input("Ingrese un número: "))
contador=0
decimal=0

while n!=0:
    residuo1=n%10
    decimal+=residuo1*(8**contador)
    n=n//10
    contador+=1
   
lista=[]
lista2=["A","B","C","D","E","F"]
while decimal!=0:
    num=decimal%16
    if num>9 and num<16:
        letra=num%10
        decimal=decimal//16
        num=decimal%16
        decimal=decimal//16
        lista.append(num)
        if decimal==0:
            break
lista1=lista[::-1]
lista3=lista2[letra]
lista1.extend(lista3)
print(lista1)
   
while decimal!=0:
    num=decimal%16
    letra=num%10
    decimal=decimal//16
    num=decimal%16
    decimal=decimal//16
    lista.append(num)
    if decimal==0:
        break
lista1=lista[::-1]
lista1.extend(lista3)
print(lista1)