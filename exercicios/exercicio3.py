##3. Faça um programa que receba do usuário o nome de um arquivo texto e mostre na tela quantas linhas este
##arquivo possui.

arquivo: str = input ("informe o nome de arquivo para abrir: ")

with open (arquivo, "r") as arq :
    linhas = arq.readlines()

print (f"Existem {len(linhas)} linhas no arquivo")