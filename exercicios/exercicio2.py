###2. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas letras são
#vogais e quantas são consoantes.

vogais :int = 0 
consoantes : int = 0 
arquivo :str = input ("Informe o nome do arquivo: ")

with open (arquivo,"r") as arq:
    linhas = arq.readlines()

for linha in linhas :
    if linha.replace ( __old"\n",__new: "").lower() in [a , e , i , o , u] : # type: ignore
        vogais = vogais +1
    else:
        consoantes = consoantes + 1 

if vogais > 0 :
    print(f"Existe {vogais} no arquivo")
else:
    print ("Nao existe  no arquivo")

if consoantes > 0 :
    print(f"Existe {consoantes} no arquivo")
else:
    print ("Nao existe  no arquivo")
