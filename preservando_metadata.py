"""
Preservando metadatas com wraps 
Metadatas -> sao dados intrisecos em arquivos 
wraps - sao funçés que envolvem elementos com diversas finalidades


def ver_log (funcao):
    def logar(*args, **kwargs):
       Eu sou uma funcao (logar) dentro de outra
       print (f"Voce esta chamando {funcao.__name__}")
       print(f"Aqui a documentação: {funcao.__doc__}")
       return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    soma dois numeros
    return a+b

#print (soma(10,29))

print (soma.__name__)#soma
print (soma.__doc__)#soma dois numeros 
"""

#resolução

from functools import wraps

def ver_log (funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
       """Eu sou uma funcao (logar) dentro de outra"""
       print (f"Voce esta chamando {funcao.__name__}")
       print(f"Aqui a documentação: {funcao.__doc__}")
       return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a,b):
    """soma dois numeros"""
    return a+b

#print (soma(10,29))

print (soma.__name__)#soma
print (soma.__doc__)#soma dois numeros 

print (help(soma))