#Pide una cedane y un caracter por teclado (valida que sea un caracter) y muestra cuantas veces aparece el caracter en la cadena

cad = input("introduce una cadena:")
while True:
    car = input("Introduce un caracter:")
    if len(car)>1:
        print("Me tienes que dar un solo caracter")
    if len(car) == 1: break

print("En la cadena",cad, "aparecen", cad.count(car),"veces el caracter,car")