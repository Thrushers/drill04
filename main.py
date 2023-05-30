import requests
from vehiculos import *

#parte 1
print("Primera parte")
print()

instancias = []

n = int(input("Cuantos vehiculos desea insertar: "))

for i in range(n):
    print(f"Ingrese datos del automovil {i+1}: ")
    marca = input("Ingrese la marca: ")
    modelo = input("Ingrese el modelo: ")
    numeroderuedas = int(input("Ingrese el numero de ruedas: "))
    velocidad = int(input("Ingrese la velocidad en km/h: "))
    cilindrada = int(input("Ingrese la cilindrada en cc: "))
    print("")
    auto = Automovil(marca,modelo,numeroderuedas,velocidad,cilindrada)
    instancias.append(auto)

print("Imprimiendo en pantalla los vehiculos:")
print("")

for index,i in enumerate(instancias):
    print(f"Datos del movil {index + 1} :")
    print(i)
    print("")
