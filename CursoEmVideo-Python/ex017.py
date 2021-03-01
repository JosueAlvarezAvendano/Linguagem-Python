# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import hypot
print('-=' * 12)
print('CALCULADOR DE HIPOTENUSA')
print('-=' * 12)
cateto_oposto = float(input('Digite o valor do Cateto Oposto: '))
cateto_adjacente = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = hypot(cateto_adjacente, cateto_oposto)
print(f'Com esses valor de Catetos, o valor da hipotenusa será {hipotenusa:.2f}')
