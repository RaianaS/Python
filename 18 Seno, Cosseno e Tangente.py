#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ângulo = float('Digie o ângulo que você deseja: ')  
seno = math.sin(math.radians(ângulo))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ângulo, seno))   
cosseno = math.cos(math.radians(ângulo))
print = ('O ângulo de {} tem o Cosseno de {:.2f}'.format(ângulo, cosseno))
tangete =  math.tan(math.radians(ângulo))
print = ('O ângulo de {} tem a Tangete de {:.2f}'.format(ângulo, tangete))

#ou,

#from math import radians, sin, cos, tan
#ângulo = float('Digie o ângulo que você deseja: ')  
#seno = sin(radians(ângulo))
#print('O ângulo de {} tem o Seno de {:.2f}'.format(ângulo, seno))   
#cosseno = cos(radians(ângulo))
#print = ('O ângulo de {} tem o Cosseno de {:.2f}'.format(ângulo, cosseno))
#tangete =  tan(radians(ângulo))
#print = ('O ângulo de {} tem a Tangete de {:.2f}'.format(ângulo, tangete))