#pacotes externos

# coloroma = permite textos coloridos no terminal

#pip instal coloroma

# utilizando o pacote
##from colorama import init,Fore
#init()

#print (Fore.GREEN + "ola Mundo")

import pydf # type: ignore
pdf = pydf.generate_pdf('<h1>this is html</h1>')
with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
