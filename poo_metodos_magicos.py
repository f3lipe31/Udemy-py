"""
Poo - MEtodos Mágicos 

sao todos metodos que utilizam dunder

dunder init __init__ -> é o construtor da classe, é o metodo que é executado quando a classe é instanciada
  def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


dunder - double underscore

 def __repr__(self):
        return f'{self.titulo} escrito por {self.autor} tem {self.paginas} paginas'
"""

class Livro():
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} escrito por {self.autor}"
        
    def __len__(self):
        return self.paginas
        
    def __del__(self):
         print("Um objeto do tipo livro foi deletado")

    def __add__(self,outro):
        return f"{self} - {outro}"
    
    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Multiplicação não suportada'

   

livro1 = Livro('Python', 'Gustavo Guanabara', 250)
livro2 = Livro('Java', 'Robert Martin', 300)

print(livro1)

print(livro2)

print(len(livro1))
print(len(livro2))

print(livro1 + livro2)

print(livro1 * 3)
