#Algoritmo que muestre la tabla de multiplicar de los numero 1,2,3,4 y 5.

for tabla in range (1, 6):
    for num in range(1, 11):
        print("%d * %d = %d" % (num,tabla,num*tabla))
        