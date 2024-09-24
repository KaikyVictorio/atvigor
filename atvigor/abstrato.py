from abc import ABC,abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area():
        pass
    @abstractmethod
    def perimetro():
        pass
    
class Retangulo(FormaGeometrica):
    def area(base,altura):
        return base*altura
    
    def perimetro(base, altura):
       return (base*2)+(altura*2)
        
class Circulo(FormaGeometrica):
    def area(r):
        return 3.14*r**2
    
    def perimetro(r):
        return 2*3.14*r
    

perimetro= Retangulo.perimetro(3,3)
print(perimetro)
perimetro1 = Circulo.perimetro(5)
print(perimetro1)

    
