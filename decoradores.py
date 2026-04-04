"""
Decoradores (decorators)

O que sao decorators?
-são funções 
-decorators envolvem outras funções e aprimnoram seus comportamentos 
decorators tem uma sintaxe propria, usando "@" (syntact sugar)

#Teste 01
#saudacao()

teste = seja_educado(saudacao)

teste()

#Teste 02
def raiva():
    print ("Te odeio")

raiva_educada = seja_educado(raiva)

raiva_educada()

#Decorators como função (sintaxe nao recomendada/ sem syntact sugar)

def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print("foi um prazer te conhecer")
        funcao()
        print("Tenha um bom dia")
    return sendo_mesmo


@seja_educado_mesmo
def apresentacao():
    print ("Meu nome é Felipe ")

#testando 
apresentacao()

@seja_educado_mesmo
def dormir():
    print ("quero dormir")

dormir()


"""




