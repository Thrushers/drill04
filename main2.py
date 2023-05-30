import requests
from vehiculos import *

#parte 2

print("Segunda parte")
print()

particular1 = Particular("Ford","Fiesta",4,180,500,5)
camion1 = Camion("Daft truck", "G 38",10,120,"1000","20000")
bicicleta1 = Bicicleta("Shimano","Mt ranger",2,"Carrera")
motocicleta1 = Motocicleta("BMW","F800s",2,"Deportiva","2T","Doble viga",21)


particular1.imprimir_particular()
print("----------------")

camion1.imprimir_camion()
print("----------------")

bicicleta1.imprimir_bicicleta()
print("----------------")

motocicleta1.imprimir_motocicleta()
print("----------------")

print("Segunda parte: instance")
print()

print(f"Motocicleta es instancia con relacion a Vehiculo: {isinstance(motocicleta1,Vehiculo)}")
print(f"Motocicleta es instancia con relacion a Automovil: {isinstance(motocicleta1,Automovil)}")
print(f"Motocicleta es instancia con relacion a Vehiculo particular: {isinstance(motocicleta1,Particular)}")
print(f"Motocicleta es instancia con relacion a Vehiculo de carga: {isinstance(motocicleta1,Camion)}")
print(f"Motocicleta es instancia con relacion a Bicicleta: {isinstance(motocicleta1,Bicicleta)}")
print(f"Motocicleta es instancia con relacion a Motocicleta: {isinstance(motocicleta1,Motocicleta)}")
