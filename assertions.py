"""
Assertions (afirmações) 
Asserções são usadas para testar se uma condição é verdadeira. Se a condição for falsa, uma AssertionError é levantada. As asserções são úteis para verificar se o código está funcionando como esperado durante o desenvolvimento e testes.

#Alerta:Cuidado ao usar assert

se um programa python ,for executado com o parametro -O (otimização), as asserções serão ignoradas e não serão avaliadas. 
Isso significa que o código dentro das asserções não será executado, o que pode levar a comportamentos inesperados se o programa depender dessas verificações para funcionar corretamente. 
Portanto, é importante usar asserções apenas para verificar condições que são críticas para o funcionamento do programa e não para validar entradas ou realizar verificações de segurança.
"""
def soma_numero_positivo(a,b):
    assert a>0 and b>0,"Ambos os números devem ser positivos"
    return a+b

ret = soma_numero_positivo(2,10)
#ret = soma_numero_positivo(-2,10)
print(ret)

def comer_fast_food(comida):
    assert comida in ['hamburguer','pizza','sorvete'], "Comida não saudável"
    return f"Comendo {comida}"

comida = input("Digite uma comida: ")
print(comer_fast_food(comida))

