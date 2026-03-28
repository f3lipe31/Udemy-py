import os  

print (os.getcwd())
res = os.path.join(os.getcwd(),'geek')

os.chdir(res)

print(os.getcwd())