#Realiza un algoritmo que muestre la tabla de multiplicar de un numero introducido por teclado.

tabla = int(input("¿De que numero quieres mostrar la tabla de multiplicar?:"))
for num in range(1, 11):
    print("%d * %d = %d" % (num,tabla,num*tabla))
    