# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan, radians
angulo = float(input('Digite um ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo digitado foi {angulo}º')
print(f'Seno: {seno:.3f}')
print(f'Cosseno: {cosseno:.3f}')
print(f'Tangente: {tangente:.3f}')
