numeros = [7,8,6,9,10]
suma = 0
for n in numeros:
    suma += n
promedio = suma / len(numeros)
print("Promedio: ", promedio)


numeros = [12,45,7,89,23]
mayor = numeros[0]
for num in numeros:
    if num > mayor:
        mayor = num
print("El mayor es: ", mayor)


numeros = [1,4,7,8,10,3]
pares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1
print("Cantidad de pares: ", pares)


lista = [5,10,15,20]
lista_invertida = []
for i in range(len(lista)-1, -1, -1):
    lista_invertida.append(lista[i])
print("Lista invertida: ", lista_invertida)


a = [1,2,3]
b = [4,5,6]
resultado = []
for i in range(len(a)):
    resultado.append(a[i] + b[i])
print("Suma: ", resultado)


lista = [1,3,5,3,9,3,7]
contador = 0
buscar = 3
for elemento in lista:
    if elemento == buscar:
        contador += 1
print("Aparece", contador, "veces")


original = [4,15,9,20,2,18]
nueva_lista = []
for n in original:
    if n > 10:
        nueva_lista.append(n)
print("Mayores a 10: ", nueva_lista)


numeros = [11,22,33,44]
buscar = 33
encontrado = False
for n in numeros:
    if n == buscar:
        encontrado = True
        break
if encontrado:
    print("Sí está en la lista")
else:
    print("No se encontró")
    
    
lista = [2,5,7,8,11]
suma = 0
for num in lista:
    if num % 2 != 0:
        suma += num
print("Suma de impares: ",suma)


lista = [4,5,4,7,5,8,4]
lista_sin_duplicados = []
for n in lista:
    if n not in lista_sin_duplicados:
        lista_sin_duplicados.append(n)
print("Lista limpia: ", lista_sin_duplicados)


numeros = [3, 6, 9]
for i in range(3):#El rango debe ser menor a 4 y mayor a 0, ya que solo hay 3 elementos en la lista
    print(numeros[i])
    
    
frutas = ["coco","papaya","melón"] #La lista debe tener elementos para funcionar.
print(frutas[0])


lista = [2, 4, 6]
suma = 0 # No había definido la variable o contador "suma".
for num in lista:
    suma += num  
print(suma)


edades = [15, 22, 30, 18]
mayores = 0
for e in edades:
    if e >= 18: #Se tenía que agregar un igual.
        mayores += 1 #Estaba mal escrito el signo.
print("Mayores de 18:", mayores)


nombres = ["Ana", "Luis", "María"]
for i in nombres: #Hacía falta "for" e "i".
    if i == "Luis":
        print("Está Luis")
        
        
numeros = [10, 20, 30]
print(f"Suma: {+ sum(numeros)}")  # Hacía falta la "f" y "{}"