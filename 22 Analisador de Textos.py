#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.

# - Nome com todas as letras maiúscula
# - Nome com todas em menúscula
# - Quantas letras ao tod (sem considerar espaços)
# - Quntas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip() #Strip elimina os espaços
print('Analisando seu nome..')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #Consigo tirar todos os espaços e tmb o do meio 
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))


#Com esse comando consigo tirar todos os espaços e tmb o do meio >>> .format(len(nome) - nome.count(' '))) <<<