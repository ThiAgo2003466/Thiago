velocidade = int(input("Digite sua velocidade:"))
km = 7
excesso = velocidade - 80
valor = excesso * km
if velocidade <= 80:
    print(f'Parabens, voce passou na velorcidade certa!')
else:
    print(f'Voce ultrapassou {excesso}Km, por isso vai pagar {valor}R$.')