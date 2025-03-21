#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Qual é seu nome completo? '))
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))

# Usando upper (maiúsculas) ou lower (minúsculas), o usuário pode digitar de qualquer forma que o nome será padronizado.
# ATENÇÃO: se eu usar 'silva' in nome.lower(), preciso garantir que o 'S' de 'Silva' esteja em minúsculas.
