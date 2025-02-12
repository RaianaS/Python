#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n = int(input('Digite um número: '))
a = n - 1
s =n + 1
#ex01
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))
#ex02
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))

#Pode ser feito de duas formas como mostra acima, pórem no "ex02" não utilizamos a variável.

