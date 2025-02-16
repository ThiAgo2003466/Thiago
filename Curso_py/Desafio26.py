distancia = int(input('Digite sua distancia de viagem:'))
primeira = distancia * 0.50
maior = distancia * 0.45
if distancia <=200:
    print(f'Voce pagara {primeira}.')
else:
    print(f'Por ser maior que 200km, voce pagara {maior}.')
