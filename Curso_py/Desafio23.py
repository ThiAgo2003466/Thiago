import random 
ale = random.randint(0,5)
tente = int(input("Digite um numero de 0 a 5 para tentar acerta o numero que o computador pensou:"))
if ale == tente:
    print("Parabens voce acertou!")
else:
    print(f"Voce errou o numero era {ale}:")

