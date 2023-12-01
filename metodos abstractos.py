from abc import ABC, abstractmethod
import os
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
    
class Triangulo(Figura):
    def __init__(self,lado1,lado2,lado3,base,altura):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura
    def perimetro(self):
        return self.lado1+self.lado2+self.lado3

class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado=lado
    
    def area(self):
        return self.lado*self.lado
    def perimetro(self):
        return self.lado*4

class Circulo(Figura):
    def __init__(self,radio):
        self.radio=radio
    
    def area(self):
        return 3.1416*self.radio**2 
    def perimetro(self):
        return 2*3.1416*self.radio
         

os.system("cls")
t1=Triangulo(5,3,5,4,6)
print("Area =",t1.area())        

c1=Circulo(6)
print("Area =",c1.area())


# EJERCICIO CON TIENDAS
# se va a crear una tienda de libros y comprar en linea dichos libros
# no se van a limitar la cantidad de libros que vamos a comprar