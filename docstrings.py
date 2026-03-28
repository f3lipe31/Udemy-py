"""
documentando funções com docstrings
"""

#exemplos 

def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'

def exponencial(num, potencia=2):
    """Função que retorna o valor de 'num' elevado à 'potencia'.
    :param numero : número que desejamos elevar
    :param potencia : potência que queremos elevar o número. Padrão é 2 (quadrado)
    :return : retorna o valor de 'num' elevado à 'potencia'
    """
    return num ** potencia
    
    
  