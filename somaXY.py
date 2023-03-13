# Faça a soma dos numeros de x a y (informados pelo usuário), desde que x seja menor que Y, e apresente o valor total(semelhante ao anterior).
x = int(input("informe o valor de x: "))
y = int(input("informe o valor de y: "))
soma = 0
for i in range(x, y + 1):
    if(x < y):
        soma += i
print(soma)
else:
    print("x deve ser menor que y")
