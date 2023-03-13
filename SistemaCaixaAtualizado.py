#8) O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. O valor “0” (zero) deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. A saída deve ser conforme o exemplo abaixo:


"""
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 10.00
Produto 4: R$ 0
Total: R$ 18.00
Dinheiro: R$ 20.00
Troco: R$ 2.00
...
"""
print("Lojas Tabajara")

produto = 0

total = 0

valor = 1

dinheiro = 0

while(valor != 0):
    valor = float(input("adicione o valor do produto:"))
    total += valor
    produto += 1
    print("Produto", produto, ": R$", valor)

print ("Total: R$ ", total)

dinheiro = float(input("adicione o valor do dinheiro depositado: "))

troco = dinheiro - total

print ("Dinheiro: R$", dinheiro)

print("Troco: R$ ", troco )
