numero=int(input("Ingrese un número de tres dígitos: "))
lista1=['','dieci','veinti','treinta y ','cuarenta y ','cincuenta y ','sesenta y ','setenta y ','ochenta y ','noventa y ']
lista2=['','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve']
lista3=['','Diez','Veinte','Treinta','Cuarenta','Cincuenta','Sesenta','Setenta','Ochenta','Noventa']
lista4=['','Once','Doce','Trece','Catorce','Quince']
lista5=['','Ciento ','Doscientos ','Trecientos ','Cuatrocientos ','Quinientos ','Seiscientos ','Setecientos ','Ochocientos ','Nuevecientos ']
if (numero<100):
    num1=numero%10
    num2=numero//10
    if(numero<10)and(numero!=0):
        print(lista2[num1])
    elif(numero>15) and (numero<100) and (numero>9) and (numero%10!=0):
        print((lista1[num2]) + (lista2[num1]))
    elif(numero<16) and (numero<100) and (numero>9):
        print(lista4[num1])
    elif(numero%10==0) and (numero<100) and (numero>9):
        print(lista3[num2])
    elif(numero==0):
        print("cero")
    else:
        print("¡Número Inválido!")

elif(numero>99)and(numero<1000):
    num1=numero//100
    num2=numero%100
    num3=num2//10
    num4=num2%10
    if(numero>99)and(numero<1000)and(numero!=100)and(num3!=1):
        print((lista5[num1]) + (lista1[num3]) + (lista2[num4]))
    elif(num3==1):
        print((lista5[num1]) + (lista4[num4]))
    elif (numero==100):
        print("Cien")
else:
    print("¡Número Inválido!")

    