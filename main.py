saldo=3000
retiro=int(input("Ingrese el monto que desea retirar: "))
if retiro==saldo:
    print(f"Retiro exitoso, su saldo actual es de: {saldo-retiro}")
elif retiro==0:
    print(f"Su saldo actual es de: {saldo-retiro}, Adiós.")
n=1
while retiro>saldo:
    print(f"Saldo insuficiente, su saldo actual es de: {saldo}")
    print("Intentelo de nuevo.")
    retiro=int(input("Ingrese el monto que desea retirar: "))
    n=n+1
    if n==3 and retiro>saldo:
        print("Se agotaron los intentos. Intentelo de nuevo en las proximas 24 horas.")
        break
if n<4 and retiro<saldo and retiro!=0:
    print (f"Retiro exitoso, su saldo actual es de: {saldo-retiro}")
