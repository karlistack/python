# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import math as m

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


class Punto(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Forma(Punto):
    
    def __init__(self, color='azul', nombre='yikes'):
        self.color = color
        self.nombre = nombre
        super(Punto,self).__init__(self,1,1)

    def imprimir(self):
        print(color, nombre,x,y)
         

    def getColor(self):
        return Forma.color

    def setColor(self):
        nuevocolor = input("introduce un color")
        self.color = nuevocolor
        return self.color

    def moverForma(self):
        nuevax = input("introduce una cordenada")
        nuevay = input("introuduce una cordenada")
        self.x = self.x + nuevax
        self.y = self.y + nuevay


class Rectangulo(Forma):
    def __init__(self, ladoMenor, ladoMayor,area=0,perimetro=0):
        self.ladoMenor = ladoMenor
        self.ladoMayor = ladoMayor
        self.area = area
        self.perimentro = perimetro

    def imprimir(self):
        print(self.ladoMayor,self.ladoMenor,self.area,self.perimentro)

    def calcularArea(self):
        area = self.ladoMenor * self.ladoMayor
        print('el area es',area)
        self.area = area
        return area

    def calculadrPerimetro(self,):
        perimetro = 2 * self.ladoMayor + 2 * self.ladoMenor
        self.perimentro = perimetro
        print('el perimetro',perimetro)

    def cambiarTamaño(self,):
        factorescala = int(input("introuce el factor"))
        areacambiada = (self.area*factorescala)
        self.area = areacambiada
        print(areacambiada)


class Elipse(Forma):
    def __init__(self,radiomayor,radiomenor,area=0,):
        self.radiomayor = radiomayor
        self.radiomenor = radiomenor
        self.area = area
   

    def calcularArea(self):
     area = m.pi*(self.radiomayor*self.radiomenor)
     print(area)
    pass


class Cuadrado(Rectangulo):
    def __init__(self, lado, area=0, perimetro=0):
        self.lado = lado

    def calcularArea(self):
        area = (self.lado)**2
        print(area)
    pass

    def calculadrPerimetro(self):
        perimetro = (self.lado)*4
        print(perimetro)

class Circulo(Elipse):
    def __init__(self, radio, area=0):
        self.radio = radio

    def calcularArea(self):
        area = m.pi*self.radio**2
        print("el area es", area)
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('estas en el main')
    e1 = Elipse(1,2)
    e1.calcularArea()
    c1 = Circulo(5)
    c1.calcularArea()
    cuadra = Cuadrado(23)
    cuadra.calcularArea()