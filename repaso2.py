"""
Un arepuerto maneja los aviones que ingresan, cada avion tiene su propia aerolinea y cada aerolinea se encarga
de registrar sus aviones con sus diferentes caracteristicas. Elabora una solución que utilice Python
para realizar este sistema.

*Si cada aerolinea quisiera implementar un registro de las salidas y entradas de los vuelos, ¿Que solución
puedes proponer? Implentala en tu código.
"""


#class Aeropuerto():
#class Avion():
#class Aerolinea:
#def registraravion():

class Aeropuerto():
    def __init__(self,nombre):
        self.nombre = nombre
        self.aerolineas = []
        self.puertas = ["Puerta 1","Puerta 2","Puerta 3","Puerta 4"]

    def __str__(self):
        return(f"***Bievenidos al aeropuerto {self.nombre}***")

class Aerolinea():
    def __init__(self,nombre,*aviones):
        self.nombre = nombre
        self.aviones = []

    def maviones(self,aviones):
        self.aviones.append(aviones)
        #print(self.aviones)
        for a in self.aviones:
            print(a)

class Aviones():
    def __init__(self,modelo,tipo):
        self.modelo = modelo
        self.tipo = tipo

    def __str__(self):
        return(f"***Datos del avión***\n"+
               f"Modelo: {self.modelo}\n"+
               f"Tipo: {self.tipo}\n")

#aerop = Aeropuerto()
#avion = Aviones("Boing 727","Comercial")
#aero = Aerolinea("Avianca",avion)
#aero.maviones()

nomb = input("Escribe el nombre del aeropuerto: ")
aerop = Aeropuerto(nomb)
print(aerop)
print("Registro de los aviones")
nomaer=input("Ingrese el nombre de la aerolínea: ")
aero=Aerolinea(nomaer)
while True: 
    mavion = input("Ingrese el modelo del avión: ")
    tavion = input("Ingrese el tipo del avión: ")
    avion = Aviones(mavion,tavion)
    aero.maviones(avion)
    op = input("Deseas ingresar otro dato? s/n")
    if(op == "n"):
        break
    else:
        continue


    
