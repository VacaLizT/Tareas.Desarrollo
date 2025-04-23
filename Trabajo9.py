num=int(input("Ingrese un número: "))
if num % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

    
lis=[1,2,3,4]
def suma_lista(lista):
        print(sum(lista))
suma_lista(lis)


def cuenta_regresiva(n):
    if n < 0:
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n-1)
cuenta_regresiva(10) 


def cuenta_ascendente(n):
    if n > 0:
        (n)
        n=n-1
        cuenta_ascendente(n)
        print (n+1)
cuenta_ascendente(10)  