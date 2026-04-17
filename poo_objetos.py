"""
Objetos sao instancias da classe - apos o mapeamento do aobjeto no 
mundo reeal para sua representação computacional, devemos criar quantos objetos
forem nescessarios. Podemos pensar nos objetos/instancias de uma classe como variaveis do tipo
definido na classe


#Instancias/ Objetos
lamp1 = Lampada ("branca", 110 , 60)
lamp1.ligar_desligar()

print (f"A lampada esta ligada? {lamp1.checa_lampada()}")

ccl = ContaCorrente (5000,20000)

user1 = Usuario ("Felipe", "Cunha","felipe@gmail.com","1233456")

"""

class Lampada:
    def __init__(self,cor,voltagem,luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada
    
    def ligar_lampada(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True
    
class ContaCorrente:
    contador = 4999

    def __init__(self,limite,saldo,cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print (f"O cliente é {self.__cliente.__Cliente}")

class Usuario:
    def __init__(self,nome,sobrenome,email,senha):
        self.__nome = nome
        self.__sobrenone = sobrenome
        self.email = email
        self.__senha = senha
    


