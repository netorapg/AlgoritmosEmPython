#Faça um programa em Python utilizando o for(um pra cada) que:
#a)Apresente os numeros de 1 a 100.
#b)Apresente os números de 100 a 1.
#c) Apresente os números pares de 1 a 100.
#d)Apresente os números impares de 1 a 100.
#e) Faça a soma dos núemros de 1 a 100 e ao final mostre apenas a soma total.
#f) Faça a soma dos núemros de x a y (informados pelo usuário), desde que x seja menor que Y, e apresente o valor total(semelhante ao anterior).
# g) Faça a multiplicação dos números de 1 a j (fatorial) e mostre o resultado final. Exemplo: Se j = 5 você deve calcular 1 * 2 * 3 * 4 * 5 = 120
"""
#a)
n1 = 1
n2 = 100
for i in range (n1, n2):
    print(i)
"""
"""
#b)
n1 = 100
n2 = 1
for i in range (n1, - n2, -1):
    print(i)
"""

"""
#c)
n1 = 1
n2 = 100
for i in range(n1, n2):
    if(i % 2) == 0:
        print(i)
"""
"""
#d)
n1 = 1
n2 = 100
for i in range(n1, n2):
    if(i % 2) != 0:
        print(i)
"""
"""
#e)
n1 = 1
n2 = 100
soma = 0
for i in range(n1, n2 +1):
    soma += i
print(soma)
"""
"""
#f)
x = int(input("informe o valor de x: "))
y = int(input("informe o valor de y: "))
soma = 0
for i in range(x, y + 1):
    if(x < y):
        soma += i
print(soma)
else:
    print("x deve ser menor que y")
 """
"""
#g)
j= int(input("adicione o valor a ser fatorado: ") )

resultado=1
for i in range(1, j + 1):
    resultado *= i

print(resultado)
"""
