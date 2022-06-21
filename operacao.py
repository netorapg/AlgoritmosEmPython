#Exec01
import random
#Menu de opções

op1 = "1"
op2 = "2"
op3 = "3"
op4 = "4"

opesco = input("escolha uma das opções: (1) (2) (3) (4):\n")

if (opesco == op1):
    print("somar dois números")
    n1 = int(input("adicione o primeiro número:\n "))
    n2 = int(input("adicione o segundo número:\n"))
    som = n1 + n2
    print ("o resultado é:\n", som)

elif (opesco == op2):
    print("Potência")
    n1 = int(input("adicione um número:\n"))
    pot = int(input("adicione a potência:\n"))
    result = n1 ** pot
    print("o resultado é:\n", result)

elif (opesco == op3):
    print("Raíz quadrada")
    n1 = int(input("adicione um número:\n"))
    result = n1 ** 0.5
    print("O resultado é:\n", result)

elif (opesco == op4):
    print("Gerar um número aleatório:\n")
    alet = random.randint (0, 100)
    print(alet)
