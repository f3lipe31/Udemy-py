"""
1. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.

"""
from datetime import date

class Pessoa:
    def __init__(self,nome:str ,data:date,email:email):
        self.__nome:str = nome
        self.__data:date = data 
        self.__email:str = email

    @property
    def nome (self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self,nome:str) -> None:
        self.__nome = nome

    @property
    def data (self) -> date:
        return self.__data
    
    @data.setter
    def data(self,data:date) -> None:
        self.__data = data
        
    @property
    def email (self) -> str:
        return self.__email
    
    @email.setter
    def email(self,email:str) -> None:
        self.__email = email
           
    def imprimir(self) -> None:
        print (f"Nome: {self.nome}")
        print (f"Data: {self.data}")
        print (f"email: {self.email}")

if __name__ == '__main__':
    p:Pessoa = Pessoa(nome= "Felipe",data= (2005,8,31), email="lipecunha@gmail")
    p.imprimir()

