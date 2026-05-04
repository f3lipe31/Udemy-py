"""
O metodo super se refere a super classe
"""

class Animal:
    def __init__(self, nome,especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self,som  ):
        return f'O {self.__nome} faz {som}'
    
class Gato(Animal):

    def __init__(self, nome,especie,raca):
        super().__init__(nome,especie)
        self.__raca = raca


felix = Gato('Felix','Gato','Persa')
felix.faz_som('Miau')

print(felix.faz_som('Miau'))