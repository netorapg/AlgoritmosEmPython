#07) Faça um programa que mostre o menu a seguir, receba a opção do usuário e os dados necessários para executar cada operação. O programa será executado repetidamente até que o usuário passe o número informado para sair do programa (opção).

"""
====== Menu Principal ======
1. Fazer a tabuada do 1 ao 10 para um número X
2. Apresentar os múltiplos de X entre 1 e 100
3. Apresentar a soma dos números de 1 a 100
4. Sair do programa

"""
print("====== Menu Principal ======")
print("1. Fazer a tabuada do 1 ao 10 para um número X")
print("2. Apresentar os múltiplos de X entre 1 e 100")
print("3. Apresentar a soma dos números de 1 a 100")
print("4. Sair do programa")

op = int(input("escolha uma das opções (1 - 4): "))

while(op != 4):
    if( op < 1 or op > 4):
        print("opção incorreta")

    if (op == 1): 
        print("Tabuada")
        x = int(input("adicione um número: "))
        tabu = 1
        while(tabu <= 10):
            result  = tabu * x
            print(x, "x", tabu, "=", result)
            tabu += 1
    
    if (op == 2):
        print("Múltiplos")
        x = int(input("adicione um número: "))
        n1 = 1
        n2 = 100
        while(n1 <= n2):
            if(n1 % x == 0):
                print(n1, "é múltiplo de ", x)
            n1 += 1

    if (op == 3):
        print("Soma dos números de 1 a 100")
        n1 = 1
        n2 = 100
        soma = 0
        while(n1 <= n2):
            soma += n1
            n1 += 1
        print(soma)
        break