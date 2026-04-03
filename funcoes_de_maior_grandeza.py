"""
Funções de maior Grandeza - Higher Order Functions - HOF

Oq significa?

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções
 que retornam outras funções como resultados ou mesmo que podemos passar funções 
como argumentos para outra função e ate mesmo criar variaveis do tipo de funções
 nos programas

OBS : Na seção de funções, nós utilizamos

#Exemplo - Definindo as funções

def somar (a,b):
    return a+b

def diminuir (a,b):
    return a-b

def multiplicar (a,b):
    return a*b

def dividir (a,b):
    return a/b

def calcular (num1,num2,funcao):
    return funcao (num1,num2)

print (calcular(4,3, somar))

print (calcular(4,3, diminuir))

print (calcular(4,3, multiplicar))

print (calcular(4,3, dividir))

#Nested Functions - Funções Aninhadas


Em Python podemos tambem ter funções dentro de funções

#Exemplo

from random import choice

def cumprimento(pessoa):
    def humor ():
        return choice (('E ai','Suma daqui','Gosto de voce'))
    return humor() + pessoa

#Testando
print (cumprimento(' Angelina '))
print (cumprimento(' Felicitci '))

#Retornando funções de outras funções 

from random import choice

def faz_me_rir():
    def rir():
        return choice (('hahahahahah','kkkkkkkkk','yayayayayaya'))
    return rir

#Testando 
rindo = faz_me_rir()
print(rindo())

"""
#Iner Functions (Funções internas) podem acessar o escopo de funções mais externas.

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice (('hahahahah','kkkkkkkkk','yayayayaya'))
        return f'{risada} {pessoa}'
    return dando_risada

#Testando 

rindo = faz_me_rir_novamente ('Pedro')

print(rindo())
print(rindo())
print(rindo())

