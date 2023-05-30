import csv

#parte 01

class Vehiculo():
    def __init__(self,marca,modelo,numeroderuedas):
        self.marca = marca
        self.modelo = modelo
        self.numeroderuedas = numeroderuedas
        
    def guardar_datos_csv(self):
        try:
            with open("vehiculos.csv", "a", newline="") as archivo:
                datos = [(self.__class__, self.__dict__)]
                archivo_csv = csv.writer(archivo)
                archivo_csv.writerows(datos)
        except FileNotFoundError:
            print("No existe vehiculos.csv")
        except Exception as e:
            print("Error reportado es : ",e)
            
    def leer_datos_csv(self):
        try:
            with open("vehiculos.csv", "r") as archivo:
                vehiculos = csv.reader(archivo)
                print(f"Lista de vehiculos {type(self).__name__}" )
                for item in vehiculos:
                    clase_vehiculo = str(self.__class__)
                    if clase_vehiculo in item[0]:
                        print(item[1])
                
        except FileNotFoundError:
            print("No existe vehiculos.csv")
        except Exception as e:
            print("Error reportado es : ",e)
    

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, numeroderuedas, velocidad, cilindrada):
        super().__init__(marca, modelo, numeroderuedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def imprimir_automovil(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nN° de ruedas: {self.numeroderuedas} \nVelocidad: {self.velocidad} \nCilindrada en cc: {self.cilindrada}")
        
    def __str__(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nN° de ruedas: {self.numeroderuedas} \nVelocidad: {self.velocidad} \nCilindrada en cc: {self.cilindrada}"        

##parte 2

class Particular(Automovil):
    def __init__(self, marca, modelo, numeroderuedas, velocidad, cilindrada, asientos):
        super().__init__(marca, modelo, numeroderuedas, velocidad, cilindrada)
        self.asientos = asientos

    def get_asientos(self):
        return self.asientos
    
    def set_asientos(self, asiento_new):
        self.asientos = asiento_new
    
    
    def imprimir_particular(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nN° de ruedas: {self.numeroderuedas} \nVelocidad: {self.velocidad} \nCilindrada en cc: {self.cilindrada} \nCantidad de asientos: {self.asientos}")
        
    def __str__(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nN° de ruedas: {self.numeroderuedas} \nVelocidad: {self.velocidad} \nCilindrada en cc: {self.cilindrada} \nCantidad de asientos: {self.asientos}"

class Camion(Automovil):
    def __init__(self, marca, modelo, numeroderuedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, numeroderuedas, velocidad, cilindrada)
        self.carga = carga
        
    def get_carga(self):
        return self.carga
    
    def set_carga(self, carga_new):
        self.carga = carga_new
           
    def imprimir_camion(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nN° de ruedas: {self.numeroderuedas} \nVelocidad: {self.velocidad} \nCilindrada en cc: {self.cilindrada} \nPeso de carga maxima: {self.carga}")
        
    def __str__(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nN° de ruedas: {self.numeroderuedas} \nVelocidad: {self.velocidad} \nCilindrada en cc: {self.cilindrada} \nPeso de carga maxima: {self.carga}"


class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, numeroderuedas, tipo):
        super().__init__(marca, modelo, numeroderuedas)
        self.tipo = tipo
        
    def imprimir_bicicleta(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nN° de ruedas: {self.numeroderuedas} \nTipo: {self.tipo}")
        
    def __str__(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nN° de ruedas: {self.numeroderuedas} \nTipo: {self.tipo}"        
        
class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, numeroderuedas, tipo, nro_radio, cuadro, motor):
        super().__init__(marca, modelo, numeroderuedas, tipo)
        self.nro_radio = nro_radio
        self.cuadro = cuadro
        self.motor = motor
        
    def imprimir_motocicleta(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo} \nN° de ruedas: {self.numeroderuedas} \nTipo: {self.tipo} \nN° de radio: {self.nro_radio} \nCuadro: {self.cuadro} \nMotor: {self.motor}")
        
    def __str__(self):
        return f"Marca: {self.marca} \nModelo: {self.modelo} \nN° de ruedas: {self.numeroderuedas} \nTipo: {self.tipo} \nN° de radio: {self.nro_radio} \nCuadro: {self.cuadro} \nMotor: {self.motor}"        
