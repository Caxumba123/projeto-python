import random
numero_secreto = random.randint(1, 100)

while True:
    chute = int(input("Digite um número entre 1 e 100: "))
    if chute < numero_secreto:
        print("O número é maior")
    elif chute > numero_secreto:
        print("O número é menor")
    else:
        break
print(f"Parabéns, o numero certo era {numero_secreto}")