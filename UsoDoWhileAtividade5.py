#5) Faça um program em Python "Acertou, Ganhou!", o programa deverá:
#a) Gerar um número aleatório entre 1 e 10 e pedir para o usuário digitar números até que acerte. Ao acertar, apresente uma mensagem parabenizando e finalize o programa.
#b) Modifique o programa anterior para contar quantas vezes o usuário digita números tentando acertar. No final, mostre uma mensagem parabenizando ele e mostrando quantas tentativas ele teve para acertar o número.
#c) Gerar um número aleatório entre 1 e 10 e pedir para o usuário digitar números até que acerte, porém, a cada erro do usuário você deve gerar um número aleatório novamente. Ou seja, a cada rodada ele gera um número diferente que o usuário tem que acertar.
#d) Modifique o programa anterior para contar quantas vezes o usuário digita números tentando acertar. No final, mostre uma mensagem parabenizando ele e mostrando quantas tentativas ele teve para acertar o número.
import random

"""
#a) e b)
rando = random.randint(1, 10)
sorte = int(input("adivinhe o número:"))
total = 0
while(sorte != rando):
        sorte = int(input("você errou, tente de novo:"))
        if(sorte == rando):
            print("você acertou")
        total += 1

if (sorte == rando):
    print("você tentou", total, "vezes até acertar")
"""

#c) e d)
"""
rando = random.randint(1, 10)
sorte = int(input("adivinhe o número:"))
total = 0
while(sorte != rando):
        rando = random.randint(1, 10)
        sorte = int(input("você errou, tente de novo:"))
        if(sorte == rando):
            print("você acertou")
        total += 1

if (sorte == rando):
    print("você tentou", total, "vezes até acertar")

"""