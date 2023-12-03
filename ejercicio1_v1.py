#Crea una aplicacion que pida un numero y calcule su factorial (El factorial de un numero es el producto de todos los enteros 
#entre 1 y el propio numero y se representa por el numero seguido de un signo de exclamacion.
#Por ejemplo 5! = 1x2x3x4x5=120)

resultado = 1
num = int(input("Dime un numero:"))
contador = 2;
while contador <= num:
    resultado = resultado * contador;
    contador = contador + 1;
print("El resultado es", resultado)