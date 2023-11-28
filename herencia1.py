import os
class animal:
    def __init__(self,especie,edad):
        self.especie=especie
        self.edad=edad
    
    #Metodo generico con implementacion particular
    def hablar(self):
        #metodo vacio
        pass

    #Metodo generico con implementacion particular
    def moverse(self):
        #metodo vacio
        pass

    #Metodo generico con implementacion particular
    def describeme(self):
        print("Soy un animal del tipo",type(self).__name__)


# Perro hereda de animal
class perro(animal):
    def __init__(self, especie, edad,dueño):
        super().__init__(especie, edad)
        self.dueño=dueño
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("caminando en 4 patas")

class vaca(animal):
    def hablar(self):
        print("Muu!")
    def moverse(self):
        print("caminando en 4 patas")

class abeja(animal):
    def hablar(self):
        print("Bzzz!")
    def moverse(self):
        print("caminando en 4 patas")
    
    #nuevo metodo
    def picar(self):
        print("Picar!")


os.system("cls")
mi_perro=perro("mamifero",10,"luis")
mi_vaca=vaca("mamifero",20)
mi_abeja=abeja("insecto",1)

mi_vaca.hablar()
mi_perro.hablar()
mi_abeja.hablar()

mi_vaca.describeme()
mi_perro.describeme()
mi_abeja.describeme()
# soy un animal de tipo vaca
# soy un animal de tipo perro
# soy un animal de tipo abeja

mi_abeja.picar()


#print(perro.__bases__)
##("class"__main__.animal)
#print(animal.__subclasses__())

class clase1:
    pass
class clase2:
    pass
class clase3(clase1,clase2):
    pass