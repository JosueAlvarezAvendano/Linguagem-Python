# O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome ds quatro alunos e mostre a ordem sorteada.
from random import shuffle
print('===================================')
print('SORTEADOR DE ORDEM DE APRESENTAÇÃO')
print('===================================')
aluno1 = str(input('Digite o nome do 1º aluno: '))
aluno2 = str(input('Digite o nome do 2º aluno: '))
aluno3 = str(input('Digite o nome do 3º aluno: '))
aluno4 = str(input('Digite o nome do 4º aluno: '))
ordem_de_apresentacao = [aluno1, aluno2, aluno3, aluno4]
shuffle(ordem_de_apresentacao)
print('========================================')
print('A ordem de apresentação será a seguinte:')
print(f'A 1º apresentação será do(a) {ordem_de_apresentacao[0]}')
print(f'A 2º apresentação será do(a) {ordem_de_apresentacao[1]}')
print(f'A 3º apresentação será do(a) {ordem_de_apresentacao[2]}')
print(f'A 4º apresentação será do(a) {ordem_de_apresentacao[3]}')
