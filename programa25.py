while True:
    try:
        x = int(input("Intorduce un numero:"))
        break
    except ValueError:
        print ("Debes introducir un numero")