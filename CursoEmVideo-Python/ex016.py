# Crie um programa que leia um numero Rela qualquer pelo teclado e mostre na tela a sua porção Inteiro.
from math import trunc
numero = float(input('Digite um número: '))
print(f'A parte inteira do número {numero} é {trunc(numero)}.')
