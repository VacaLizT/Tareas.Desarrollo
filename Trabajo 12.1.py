a=[[1,2],
   [3,4]]
b=[[5,6],
   [7,8]]
matriz_suma=[]
for i in range(2):
    fila_suma=[]
    for j in range(2):
        suma=a[i][j]+b[i][j]
        fila_suma.append(suma)
    matriz_suma.append(fila_suma)
(f"{a+b}")
print(matriz_suma[0])
print(matriz_suma[1])



c=[[1,2],
   [3,4]]
d=[[5,6],
   [7,8]]
matriz_resta=[]
for i in range(2):
    fila_resta=[]
    for j in range(2):
        resta=c[i][j]-d[i][j]
        fila_resta.append(resta)
    matriz_resta.append(fila_resta)
print(matriz_resta[0])
print(matriz_resta[1])



e=[[1,2],
   [3,4]]
matriz_mul=[]
for i in range(2):
    fila_mul=[]
    for j in range(2):
        mul=e[i][j]*2
        fila_mul.append(mul)
    matriz_mul.append(fila_mul)
print(matriz_mul[0])
print(matriz_mul[1])


f=[[1,2],
   [3,4]]
matriz_tra=[]
for i in range(2):
    fila_tra=[]
    for j in range(2):
        fila_tra.append(f[j][i])
    matriz_tra.append(fila_tra)
print(matriz_tra[0])
print(matriz_tra[1])
