valor = int(input("Digite um valor para saber se é par ou impar:"))
par = valor % valor
impar = valor >= 1
if par <=0:
    print(f'Esse é um numero par.')
else:
    print(f"Esse é um numero impar.")