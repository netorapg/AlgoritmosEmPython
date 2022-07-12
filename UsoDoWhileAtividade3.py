#3) Na matemática, o fatorial de um número natural n, representado por n!, é o produto de todos os inteiros positivos menores ou iguais a n. Por exemplo: o fatorial de 5 é representado por 5! que é igual a 5 x 4 x 3 x 2 x 1. Faça um programa que peça um número para o usuário e apresente na tela seu fatorial.
num = int(input("Fatorial de: "))

result = 1
count = 1

while count <= num:
    result *= count 
    count += 1

print(result)