#06) Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários para executar cada operação. O programa será executado repetidamente até que o usuário passe o número informado para sair do programa (opção).

"""
====== Menu Principal ======
1. Par ou ímpar?
2. Potência XY
3. Raiz quadrada
4. Sair
"""
print("====== Menu Principal ======")
print("1. Par ou ímpar?")
print("2. Potência X^Y")
print("3. Raiz quadrada")
print("4. Sair")

op = int(input("escolha uma das opções (1 - 4): "))


while (op != 4):
    
    if( op < 1 or op > 4):
        print("opção incorreta")


    if (op == 1):
        print("Par ou Impar?")
        parouimpar = int(input("digite um número que direi se é par ou ímpar:"))
        if(parouimpar % 2 == 0):
            print(parouimpar, "é par.")
        else:
            print(parouimpar, "é ímpar")
        

    if (op == 2):
        print("Potência X^Y")
        num = int(input("adicione o número: "))
        potencia = int(input("agora a potência: "))
        total = num ** potencia
        print(total)
        

    if (op == 3):
        print("Raíz Quadrada")
        num = int(input("digite um número: "))
        raiz = num ** 2
        print(raiz)
        


    if(op == 4):
        print("Saindo do programa, até breve")

    op = int(input("escolha uma das opções (1 - 4): "))
