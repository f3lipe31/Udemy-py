from io import StringIO

mensagem = "Esta é apenas uma string normal"

arquivo = StringIO(mensagem)

print(arquivo.read)

arquivo.write("Outro texto")