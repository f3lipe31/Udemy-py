"""
Decorators com diferentes assinaturas 

#Para resolver utilizamos um padrao de projetos chamados Decorator patter 

#relembrando 

def gritar (funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f"Ola, eu sou o/a {nome}"

@gritar
def ordenar (principal,acompanhamento):
    return f"Ola, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor. "

#Testando

#print (saudacao("Angelina"))

print (ordenar("picanha","batata frita"))

#para resolver, utilizamos um padrao de projeto chamado decorator pattern

A ssinatura de uma função é representada pelo seu retorno, nome e parametros de entrada

#Refatorando com a decorator pattern

def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao (*args , **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f"Ola sou {nome} "

@gritar
def ordenar (principal , acompanhamento):
    return f"Ola eu gostaria {principal} e acompanhado de {acompanhamento}, pf. "

#Teste 

print (saudacao("Felipe"))

print (ordenar("Picanha", "batata"))

@gritar
def lol():
    return "lol"

print (lol())


"""

#Decorators com argumentos 

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra (*args , **kwargs ):
            if args and args [0] != valor:
                return f"valor incorreto! Primeiro argumento precisa ser {valor}"
            return funcao (*args,**kwargs)
        return outra 
    return interna

@verifica_primeiro_argumento("pizza")
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

#teste

print (soma_dez(10,12))

print(soma_dez(1,21))

print(comida_favorita("pizza","arroz"))

print(comida_favorita("arroz","pizza"))
    
