#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Em que cidade você nasceu? ')).strip() #Com o .strip eu removo todos os espaços
print(cid[:5].upper == 'Santo') 

#.upper() eu consigo fazer com que o nome Santo seja verdadeiro independente de como o usuario digitar ex: SaNTo
