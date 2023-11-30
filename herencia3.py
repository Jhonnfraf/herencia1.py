import os
class SeleccionFutbol:                                                                      #CLASE SELECCION DE FUTBOL
    def __init__(self,id,nombre,apellido,edad):
        self.id=id
        self.nombre=nombre
        self.edad=edad
        self.apellido=apellido
        
    #metodos
    def concentrarse(self):
        print("concentrarse")
    def viajar(self):
        print("viajar")
 
        
class futbolista(SeleccionFutbol):                                                          #CLASE FUTBOLISTA
    def __init__(self, id, nombre, apellido, edad,dorsal,demarcacion):
        super().__init__(id, nombre, apellido, edad)
        self.dorsal=dorsal
        self.demarcacion=demarcacion
        
    #metodos
    def jugarPartido(self):
        print("jugar partido")
    def entrenar(self):
        print("Entrena")


class entrenador(SeleccionFutbol):                                                          #CLASE ENTRENADOR
    def __init__(self, id, nombre, apellido, edad,idFederacion):
        super().__init__(id, nombre, apellido, edad)
        self.idFederacion=idFederacion
        
    #metodos
    def dirigirPartido(self):
        print("dirige un partido")
    def dirigirEntrenamiento(self):
        print("Dirige entrenamiento")
        
        
class masajista(SeleccionFutbol):                                                           #CLASE MASAJISTA
    def __init__(self, id, nombre, apellido, edad,titulacion ,aniosDeExperiencia):
        super().__init__(id, nombre, apellido, edad)
        self.aniosDeExperiencia=aniosDeExperiencia
        self.titulacion=titulacion
    
    #metodos
    def darMasaje(self):
        print("Da un masaje")


#                                                                                           #INICIO DE EJECUCION DEL PROGRAMA
os.system("cls")
        
integrantes=[]

delBosque=entrenador(1,"Vicente","Del Bosque",60,"Federacion española de futbol")
iniesta=futbolista(2,"Andres","Iniesta",29,6,"Interior derecho")
raulMartinez=masajista(3,"Raul","Martinez",30,"Licenciado en fisioterapia",30)

integrantes.append(delBosque)
integrantes.append(iniesta)
integrantes.append(raulMartinez)

# concentrar a todos los integrantes

print("Todos los integrantes inician una concentracion")
for i in integrantes:
    print(f"{i.nombre} {i.apellido}")
    i.concentrarse()
    #Todos ejecutaran el metodo concentrarse
    
# Viajes

print("\nTodos los integrantes van a viajar")
for integrante in integrantes:
    print(f"{integrante.nombre} {integrante.apellido}")
    integrante.viajar()
    #todos ejecutaran el metodo Viajar
        
        
        