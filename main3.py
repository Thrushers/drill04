import requests
from vehiculos import *


print("Tercera parte")
print()

particular1 = Particular("Ford","Fiesta",4,180,500,5)
camion1 = Camion("Daft truck", "G 38",10,120,"1000","20000")
bicicleta1 = Bicicleta("Shimano","Mt ranger",2,"Carrera")
motocicleta1 = Motocicleta("BMW","F800s",2,"Deportiva","2T","Doble viga",21)

particular1.guardar_datos_csv()
camion1.guardar_datos_csv()
bicicleta1.guardar_datos_csv()
motocicleta1.guardar_datos_csv()

particular1.leer_datos_csv()
camion1.leer_datos_csv()
bicicleta1.leer_datos_csv()
motocicleta1.leer_datos_csv()