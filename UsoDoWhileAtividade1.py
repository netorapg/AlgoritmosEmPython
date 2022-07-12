#1)Faça algoritmos em Python, utilizando o while, que:
#a)Apresente na tela os números de 1 a 100.
#b)Faça a soma dos números de 1 a 100 e apresente somente o resultado.
#c)Apresente na tela somente os números pares entre 50 e 100.
#d)Apresente na tela somente os números ímpares entre 1 e 50.
#eApresente na tela somente a soma dos números pares entre 1 e 100.
#f)Apresente na tela os números de X a Y (peça para o usuário informar os valores de X e de Y).
#g)Faça a soma dos números de X a Y e apresente somente o resultado (peça para o usuário informar os valores de X e de Y).
#h)Apresente na tela somente os números ímpares entre X e Y (peça para o usuário informar os valores de X e de Y).

"""
#a)
n1 = 1
n2 = 100

while(n1 < n2):
    n1 += 1
    print(n1)
"""
"""
#b)
n1 = 1
n2 = 100
soma = 0
while(n1 <= n2):
    soma += n1
    n1 += 1

print(soma) 
"""
"""
#c)
n1 = 50
n2 = 100
while(n1 <= n2):

    if( n1 %2 == 0):
        print(n1)
    n1 += 1
"""
"""
#d)
n1 = 1
n2 = 50
while(n1 <= n2):

    if( n1 %2 != 0):
        print(n1)
    n1 += 1
"""
"""
#e) 
n1 = 1
n2 = 100
soma = 0
while(n1 <= n2):

    if( n1 %2 == 0):
        soma += n1
    n1 += 1
print(soma)
"""
"""
#f)
x = int(input("adicione o valor de X: "))
y = int(input("adicione o valor de Y: ")) 

while (x <= y):
    print(x)
    x += 1
"""
"""
#g) Verificar como fazer
x = int(input("adicione o valor de X: "))
y = int(input("adicione o valor de Y: ")) 
soma = 0
while (x <= y):
    x += 1
    soma += 1
    
print(soma)
"""
"""
#h)
x = int(input("adicone o valor de x: "))
y = int(input("adicione o valor de y: "))
while(x <= y):

    if( x %2 == 0):
        print(x)
    x += 1
"""


