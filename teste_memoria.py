#Função usando lista
def fib_lista(max):
    nums = []
    a, b = 0, 1 
    while len (nums) <max:
        nums.append(b)
        a, b = b, a+b
    return nums

for n in fib_lista (10):
    print (n)    
#Função usando geratores

def fib_gen(max):
    a, b , contador = 0 , 1 , 0
    while contador < max:
        a, b = b , a+b
        yield a 
        contador = contador +1