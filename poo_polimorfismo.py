"""
poli -  Muitos
morfis  - formas
"""

class Animal(object):
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse metodo')
    
    def comer(self):
        print(f'{self.__nome} esta comendo')

class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self.Animal__nome} fala au au")

class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self.Animal__nome} fala miau miau")

class Rato(Animal):
    def __init__ (self, nome):
        super().__init__(nome)
    def falar(self):
        print(f"{self.Animal__nome} fala squeak squeak")


#teste

felix = Gato('Felix')
felix.falar()  
felix.comer()

pluto = Cachorro('Pluto')
pluto.falar()
pluto.comer()

mickey = Rato('Mickey')
mickey.falar()
mickey.comer()