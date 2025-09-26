pares = 0
impar = 0
for i in range(10):
    numeros = int(input("Digite um número: "))
    if numeros % 2 == 0:
        pares += 1
    else:
        impar += 1
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de numeros impares: {impar}")