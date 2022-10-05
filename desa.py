import random


def criarVetor():
   
    v1 = [0]*x

    for i in range (0, len(v1)):
        v1[i] = random.randint(1, 200) 
    
    return v1

def exibirVetor(v1):
    for i in range(0, len(v1)):
        print(v1[i])


def SomaImpar(v1):
    soma = 0
    for i in range(0, len(v1)):
        if(v1[i] % 2 != 0):
            soma += v1[i]
    return soma

def busca(v1):
    valor = int(input("Defina o valor a ser pesquisado: "))
    i_valor = -1
    for i in range(0, len(v1)):
        if(v1[i] == valor):
            i_valor = i
            break
    
    if(i_valor >= 0):
        print(valor, "Está no vetor")
        print("Na posição", i_valor)
    else:
        print("O número não se encontra no vetor")


def ordenar(v1, met):
    if(met == "bolha".upper()):
        for ciclos in range(0, len(v1)-1):
            for i in range(0, len(v1)-1):
                if(v1[i] > v1[i+1]):
                    temp = v1[i]
                    v1[i] = v1[i+1]
                    v1[i+1] = temp
        for i in range(0, len(v1)):
            print(v1[i])

    
    if(met == "inserção".upper()):
        for i in range(1, len(v1)):
            valor = v1[i]
            anterior = i-1

            while(anterior >= 0 and v1[anterior] > valor):
                v1[anterior+1] = v1[anterior]
                anterior -= 1
            v1[anterior+1] = valor

        for i in range (0, len(v1)):
            print(v1[i])
        
    if(met == "seleção".upper()):
        for i in range(0, len(v1)-1):
            v_menor = v1[i]
            i_menor = i 

            for j in range(i+1, len(v1)):
                if(v[j] < v_menor):
                    v_menor = v[j]
                    i_menor = j 
            temp = v[i]
            v[i] = v_menor 
            v[i_menor] = temp 
            
            for i in range(0, len(v1)):
                print(v1[i])



x = int(input("Insira o tamanho do vetor:"))
v = criarVetor()
exibirVetor(v)
print(SomaImpar(v))
busca(v)
met = input("Defina o metodo de ordenação:")
ordenar(v, met)



