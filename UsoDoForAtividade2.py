#2) Faça um programa que leia 5 números e informe apenas o maior número.
list = []

for n in range(0, 5):
    list.append(int(input("Digite o número:")))

print ("Maior número da lista: ", max(list))