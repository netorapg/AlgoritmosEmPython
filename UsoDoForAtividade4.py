#04) Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
n1 = 1
n2 = 50
for i in range(n1, n2):
    if(i % 2) != 0:
        print(i)