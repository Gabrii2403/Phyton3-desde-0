#Suponiendo que hermos introducido una cadena por teclado que representa una frase
#(palabras separadas por espacios), realiza un programa que cuente cuantas paabras tiene.

cont = 0
posicion = 0
cad = input("Introduce una cadena:")
#Elimino los posibles espacios que hay al principio y final de la cadena
cad = cad.strip()
#Voy buscando los espacios
posicion = cad.find(" ", posicion)
while posicion != -1:
    cont = cont + 1
    #No tenfo en cuenta los posibles que haya entre las palabras
    while cad[posicion + 1] == " ":
        posicion = posicion + 1
    posicion = cad.find(" ", posicion + 1)
print("La frase tiene",cont + 1, "palabras.")