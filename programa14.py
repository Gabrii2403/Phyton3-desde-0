#Escribe un programa que diga si un numero introducido por teclado es o no primo. 
#Un numero primo es aquel que solo es divisible entre el mismo y la unidad. 
#Nota: Es suficiente probar hasta la raiz cuadrada del numero para ver si es visible por algun otro numero.

es_primo = True
numero_es_primo = int(input("Introduce un numero para comprobar si es primo:"))
for num in range(2, numero_es_primo):
    if numero_es_primo % num == 0:
        es_primo = False
        break
if es_primo:
    print("Es primo")
else:
    print("No es primo")