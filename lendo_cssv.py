"""
Lendo arquivos  CSV 

CSV - Comma Separated Values (Valores Separados por Vírgula)

#Separador por virgula 

1, 2, 3, 4, 5

"genesis", "exodus", "leviticus", "numbers", "deuteronomy"

#Separador por ponto e virgula

1; 2; 3; 4; 5
"genesis"; "exodus"; "leviticus"; "numbers"; "deuteronomy"

#separador por espaço

1 2 3 4 5
"genesis" "exodus" "leviticus" "numbers" "deuter




with open ('lutadores.csv') as arquivo:
    dados = arquivo.read()
    #print(type(dados))
    print(dados)

    """

#Reader 

from csv import reader

with open ('lutadores.csv') as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        print(f"{linha[0]} nasceu em {linha[1]} e tem {linha[2]} anos")