from random import random

def jogar_moeda():
    valor = random()
    if valor > 0.5:
        return 'Cara'
    else:
        return 'Coroa'
    
print(jogar_moeda())