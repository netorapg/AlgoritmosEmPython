#2) Faça um programa para calcular a tabuada:
#a) do 1 ao 10 para um número informado pelo usuário.
#b) do X ao Y para um número informado pelo usuário (o usuário também deve informar os valores de X e Y).
"""
#a)
num = int(input("insira um número para saber sua tabuada:"))
tabu = 1
while(tabu <= 10):
    result  = tabu * num
    print(num, "x", tabu, "=", result)
    tabu += 1
"""
#b)
num = int(input("insira um número para saber sua tabuada:"))
x = int(input("informe o inicio da tabuada:"))
y = int(input("informe o fim da tabuada: "))
while(x <= y):
    result  = x * num
    print(num, "x", x, "=", result)
    x += 1