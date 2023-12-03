#Escribe un programa que pida un nombre de usuario y una contraseña
#y si se ha intorducido "pepe" y "asdasd" se inidica "Has entrado al sistema"
#sino se da un error

usuario = input("Introduce el usuario:")
password = input("Introduce el password:")
if usuario == "pepe" and password == "asdasd":
    print("Has entrado al sistema")
else:
    print("Usuario/password incorrecto")
    