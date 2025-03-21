#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))










# OBS: O +1 significa que a contagem dos caracteres começa em 1 e não em 0, para que o resultado corresponda à numeração tradicional.  
# O .upper() garante que, independentemente de o usuário digitar em maiúsculas ou minúsculas, a identificação será feita corretamente.  
# O .rfind('A') serve para localizar a última ocorrência da letra 'A', contando a partir do lado direito da string.  
