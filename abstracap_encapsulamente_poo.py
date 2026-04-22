"""
Poo - Abstração e encpsulamento


imagina que temos uma classe chamada pessoa , contendo um atributo privado chamado 
__nome e um metodo privado chamado __falar()

esses elementos privados so devem ser acessados dentro da classe. Mas Python não 
bloqueia este acesso fora da classe.Com python acontece Name Manglinf, que faz uma altecação 
na forma de se acessar os elementos privados,conforme:

_Classe__elemento

ex acessando elementos privados fora da classe

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração em poo, é o ato de expor apenas dados relevantes de uma classe
escondendo atributos e metodos privados do usuario.

conta1.extrato()

print (conta1._Conta__titular)#Name Mangling

conta1._Conta__titular = "Felipe"

print (conta1.__dict__)

print (conta1.__dict__)

conta1 .depositar(150)

print (conta1.__dict__)

conta1.sacar (2000)
print (conta1.__dict__)


"""

class Conta:
    contador = 400

    def __init__(self,titular,saldo,limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador  += 1

    def extrato(self):
        print (f"Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}" )

    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print (f"O valor {(valor)} precisa ser positivo")
        

    def sacar (self,valor):
        if valor >0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print ("Saldo insuficiente")
        else:
            print("O valor precisa ser positivo")
    
    def transferir(self,valor,conta_destino):
        #1 Transferindo o valor conta de origem
        self.__saldo -= valor
        self.__saldo -=10 #Taxa de transferencia

        #2 Adicionar o valor na conta destino
        conta_destino.__saldo += valor


# TEstando

conta1 = Conta("Geek",150.00,15000)
conta1.extrato()

conta2 = Conta ("Felipe",300,2000)
conta2.extrato()

conta2.transferir(100,conta1)

conta1.extrato()
conta2.extrato()


