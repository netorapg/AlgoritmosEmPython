#Faça a multiplicação dos números de 1 a j (fatorial) e mostre o resultado final. Exemplo: Se j = 5 você deve calcular 1 * 2 * 3 * 4 * 5 = 120
j= int(input("adicione o valor a ser fatorado: ") )
resultado=1
for i in range(1, j + 1):
    resultado *= i
print(resultado)
