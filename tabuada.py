#Utilizando o laço de repetição for, faça um programa que apresente as tabuadas do 1 ao 10 para um número informado pelo usuário.

num = int(input("digite um número: "))

tabu = 0

for i in range(1, 10 + 1):
    
    tabu = num * i
    print(tabu)
