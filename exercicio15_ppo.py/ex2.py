
""""
2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
a) armazenar_contato(contato: Contato);
b) remover_contato(contato: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda.
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.
"""

from datetime import date

from ex1 import Pessoa

class Agenda:
    def __init__(self):
        self.__contatos : list[Pessoa]= []

        @property
        def contatos(self) -> list[Pessoa]:
            return self.__contatos
        
        def armazenar_contato(self,contato: Pessoa) -> None :
            self.contatos.append(contato)

        def remover_contato(self,contato: Pessoa) -> None:
            self.contatos.remove(contato)

        def buscar_contato(self,nome:str) -> None:
            for indice, contato in enumerate(self.contatos):
                if contato.nome == nome:
                    print(f"O contato {nome} esta na posição {indice}")

        def imprimir_agenda(self) -> None:
            for contato in self.contatos:
                contato.imprimir()
        
        def imprimir_contato(self , indice: int) -> None:
            self.contatos[indice].imprimir()

if __name__ == '__main__':
    p1:Pessoa = Pessoa(nome= "Felipe",data= (2005,8,31), email="lipecunha@gmail")
    p2:Pessoa = Pessoa(nome= "Pedro",data= (2020,2,25), email="pedro@gmail")
    p3:Pessoa = Pessoa(nome= "Milena",data= (2005,6,24), email="milena@gmail")

    agenda: Agenda = Agenda()

    agenda.armazenar_contato (p1)
    agenda.armazenar_contato (p2)
    agenda.armazenar_contato (p3)

    agenda.imprimir_agenda()

    agenda.buscar_contato("Milena")

    agenda.imprimir_contatp(2)

    agenda.remover_contato (p2)

    agenda.imprimir_agenda()

    
