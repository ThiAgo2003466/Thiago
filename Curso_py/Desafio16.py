import math
oposto = float(input("Digite o valor do cateto oposto:"))
adjacente = float(input("Digite o valor do cateto adjacente:"))
oposto1 = oposto ** 2
adjacente1 = adjacente ** 2 
a = adjacente1 + oposto1
hipo = math.sqrt(a)
print(f'A soma dos dois catetos é {a} e o comprimento é {hipo}')
  
