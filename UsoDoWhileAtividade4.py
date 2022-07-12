#4) Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que peça ao usuário qual o termo final (N) e calcule o valor de H. 
#Tentar achar uma maneira
print("Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N")
n = int(input("Informe o valor de n:"))

resultado = 0
i = 1
while(i <= n):
    resultado = resultado + (1 / i)
    i += 1
print("O valor de H é:", resultado)