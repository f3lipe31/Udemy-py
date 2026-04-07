"""
Atributos representam as caracteristicas do objeto. Ou seja , pelos atributos
conseguimos representar computacionalmente os estados do objt,.

em python dividimos os atibustos em 3 grupos 
  -de instancia
  - de classe
  - dinamicos

  
  #Atributos de instancia:sao declarados dentro do metodo construto

  metodo contrutor : é um metodo utilizado para construção do objeto

  
em python por convenção  ficou estabelecido que todo atributo de uma classe é publico.
Ou seja, pd ser acessado em todo o projeto
caso queira determinar um atributo como privado- utiliza __ dulplo undescore no inicio do nome
  
p1 = Produto("play4","video game",2300)
p2 = Produto("Xbox","video game",4500)

print(p1.valor)
print(p2.valor)

print (Produto.imposto)
        
print(p1.id)
print(p2.id)        
  
  """
#Classes com atributos de instacia publica
class Lamapda:
    
    def __init__(self,voltagem,cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:
    def __init__(self,numero,limite,saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo
        

class Produto:
    def __init__(self, nome,descricao,valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

class Usuario:
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha 
    

#Atributos publicos e privados
class Acesso:
    def __init__(self,email,senha):
        self.email = email
        self.__senha = senha
    
    def mostrar_senha(self):
        print(self.__senha)

    def mostrar_email(self):
        print(self.email)

#Atributos de classe
#sao declarados diretamente na classe, fora do construtor.Geralmente ja inicializa um valor
#e este valor é compartilhado entre todas as instancias da classe.Ou seja todas as
# instancias tem o mesmo valor

#Exemplo 
class Produto:
    #Atributo classe
    imposto = 1.05 # 0.05% de imposto
    contador = 0


    def __init__(self,nome,descricao,valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id

#Atributos dinamicos - pd ser criado em tempo de execução

#OBS - o atributo dinamico sera exclusivo da instancia que o criou

p1 = Produto ("play4 ","games",2300)
p2 = Produto ("Arroz","mercearia",5.99)
#criando atributo dinamico em tempo de execução
p2.peso = "5kg"

print(f"Produto:{p2.nome}, Descrição:{p2.descricao}, valor:{p2.valor}, peso: {p2.peso   }")
print(f"Produto:{p1.nome}, Descrição:{p1.descricao}, valor:{p1.valor}")

#Deletando atributos 
print(p1.__dict__)
print(p2.__dict__)

del p2.peso
del p2.valor
del p2.descricao

print(p1.__dict__)
print(p2.__dict__)