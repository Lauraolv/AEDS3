#Escreva um programa Python que leia um tamanho n e imprima o seguinte quadrado
#formado por asteriscos

n = int (input("Digite o tamanho do quadrado: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == (n-1) or j == 0 or j == (n-1):
            print(" * ", end="")
        else:
            print("   ", end="")
    print()  

