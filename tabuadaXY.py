#Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do X a Y para um número informado pelo usuário (semelhante ao anterior, porém o usuário precisa informar três números).
num = int(input("digite um número: "))
x = int(input("adicione o inicio da tabuada: "))
y = int(input("adicione o fim da tabuada: "))
tabu = 0

for i in range(x, y + 1):
    
    tabu = num * i
    print(tabu)
