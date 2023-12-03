import random
def CalcularMaxMin(lista):
    return (max(lista),min(lista))

numeros = []

for i in range(10):
    numeros.append(random.radint(1,100))
vmax,vmin = CalcularMaxMin(numeros)
print("El valor maximo es ,vmax")
print("El valor minimo es ",vmin)
