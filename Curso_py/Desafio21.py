nome = (input('Digite seu nome:'))
print(nome.upper())
print(nome.lower())
print(len(nome))
primeiro_nome = nome.split()[0]  # Pega o primeiro nome
quantidade_letras = len(primeiro_nome)  # Conta o número de letras
print(quantidade_letras)