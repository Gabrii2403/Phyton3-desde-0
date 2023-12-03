#Crea una aplicacion que pida un numero y calcule su factorial (El factorial de un numero es el producto de todos los enteros 
#entre 1 y el propio numero y se representa por el numero seguido de un signo de exclamacion.
#Por ejemplo 5! = 1x2x3x4x5=120)

resultado = 1
num = int(input("Dime un numero:"))
for contador in range(2, num+1):
    resultado = resultado * contador;
print("El resultado es", resultado)