"""
Metodos - representam comportamentos,ou seja,as acções que este
objeto pode realizar no sistema

em python sao deivididos em 2 grupos. Metodos de instancia e de classe

o metodo dunder __init__ é um metodo construtor que controi 
a partir da classe

dunder = __ (double underline)

nome = input ("Digite seu nome: ")
sobrenome = input ("Digite seu sobrenome: ")
email = input ("Digite seu email: ")
senha  = input ("Digite sua senha: ")
confirma_senha = input ("Confirme sua senha")


if senha == confirma_senha:
    user = Usuario(nome,sobrenome,email,senha)
else:
    print("Senhas diferentes")

print ("Usuario criado com sucesso")

senha = input ("Informa a senha novamente: ")
if user.checa_senha(senha):
    print("Acesso permitido")
else:
    print("Acesso negado")

    #Metodos de classe
 

Usuario.conta_usuarios() # Forma correta
user.conta_usuarios() #Possivel, mas incorreta


"""

class Lampada:
    def __init__(self,cor ,voltagem,luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 4999
    
    def __init__(self,numero,limite,saldo):
        self.__numero = ContaCorrente.contador +1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero
        
class Produto:

    contador = 0

    def __init__(self,nome,descricao,valor):
        self.__id = Produto.contador +1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id
    def desconto(self,porcetagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - porcetagem)) / 100
    
from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    def __init__(self,nome,sobrenome,email,senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.encrypt(senha, round = 200000, salt_size = 16)
        Usuario.contador = self.__id
        print(f"Usuario criado:{self.__gera__usuario()}")
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

def __gera_usuario(self):
    return self.__email.split ("@")[0]

user = Usuario ("Felicity", "Jones", "felicity@gmail.com" , "123456")


