#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
#El tiempo de viaje hasta llegar a otra ciudad B es de T segubdos.
#Escribir un algortimo que determine la hora de llegada a la ciudad B.

horapartida = int(input("Hora de salida:"))
minpartida = int(input("Minutos de salida:"))
segpartida = int(input("Segundos de salida:"))
segviaje = int(input("Tiempo que has tardado en segundos:"))
#Convierto la hora de salida a segundos
seginicial = horapartida * 3600 + minpartida*60 + segpartida;
#Le sumo os segundos que he tardado
segfinal = seginicial + segviaje;
#Convierto los segundos totales a hora, minutos y segundos
horallegada = segfinal // 3600;
minllegada = (segfinal % 3600) // 60;
segllegada = (segfinal % 3600) % 60;
#Muestro la hora de llegada
print("Hora de llegada")
print(horallegada,":",minllegada,":",segllegada)