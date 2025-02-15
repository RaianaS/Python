#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Primeira nota do aluno: ')) #float é para número flutuantes que contem ponto, peso, km..
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2  #Juntei a nota a1 com a2 e depois dividir por 2 trazendo o resultado da média. #d = s/2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, m))