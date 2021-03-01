#FATIAMENTO

frase = 'Curso em Video Python'  #O indice começa no 0 e vai até 0 fim
print(frase[6])                  #Mostra o que está dentro do indice NomeLista[um numero + 1]
print(frase[4:10])               #Dentro da lista NomeLista[inicio : mostra ate o numero menos um]
print(frase[6:13:2])             #Dentro da lista NomeLista[inicio: 1 depois do fim : passo]
print(frase[:5])                 #Mostra desde o inico até um numero antes representado
print(frase[3::2])               #Mostra do inicio pedido e vai até o fim pulando o numero do passo

print('''Texto é um conjunto de palavras e frases encadeadas, 
que permitem interpretação e transmitem uma mensagem.
É qualquer obra escrita em versão original e que constitui um livro ou um documento escrito.
Um texto é uma unidade linguística de extensão superior à frase.''')
#Colocar ''' no começo e ''' no fim mostra o texto no mesmo formato que está

#ANALISE

print(len(frase))                #Mostra quantos espaços(mostra a quantidades de str tem mais 1) tem a lista[]
print(frase.count('o'))          #Mostra quantas vesez aparece o que está dentro dos parenteses
print(frase.count('o',0,13))     #Mostra quantas vezes aparece o que se pede dentro de um incio e fim (fim-1)
print(frase.find('deo'))         #Mostra onde(iniciou) foi encontrato o que se pede
print(frase.find('Josué'))       #Se eu pedir algo que não está na lista, me mostrara -1
print('Curso' in frase)          #Pergunta se existe algo na frase

#TRANSFORMAÇÂO

print(frase.replace('Python','Android'))  #Troca algo por outra coisa
print(frase.upper())                      #Coloca tudo em maiúsculos
print(frase.lower())                      #Coloca tudo em minúsculo
print(frase.capitalize())                 #Deixa tudo em minusculo e deixa só o primeiro em maiusculos
print(frase.title())                      #Deixa todos as primeiras letras de palavra em maiuscula
print(frase.strip())                      #Remove os espaços a mais no começo e no fim (não remove espaços no meio)
print(frase.rstrip())      #R = Direita   #Só vai remover os espaços a mais na direita (ou seja no fim)
print(frase.lstrip())      #L = Esquerda  #Só vai remover os espaços a mais na esquerda (ou seja no começo)

#DIVISÂO

print(frase.split())              #Vai separar cada palavra e transformar em uma str e coloca em uma nova lista
lista = frase.split()

#JUNÇÂO

print(' '.join(lista))            #Vai juntar palavras em uma lista colocando ' ' entre elas


#Você pode fazer junção das funções