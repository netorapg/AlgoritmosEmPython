import random
import time
n1 = float(input("insira o menor valor: "))
time.sleep(2)
n2 = float(input("insira o maior valor: "))
time.sleep(2
)
if(n1 > n2):
    swap = n1 
    n1 = n2 
    n2 = swap 
print("Gerando números...")
time.sleep(5)
print
x = random.randint(n1, n2)
print(x)
time.sleep(4)
y = random.randint(n1, n2)
print(y)
time.sleep(4)

if(x > y):
    print("o maior valor é", x)

elif (x == y):
    print("os valores são os mesmos")

else:
    print("o maior valor é", y)


    