# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))


#Existe três formas para fazer:

#from math import trunc
#num = float(input('Digite um valor: '))
#print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))


#num = float(input('Digite um valor: '))
#print('O valor digitando foi {} e a sua porção inteira é {}'.format(num, int(num)))