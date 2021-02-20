# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessaria para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input('Qual a largura da parede em metros: '))
altura = float(input('Qual a altura da parede em metro: '))
area = largura * altura
tinta = area / 2
print(f'A área da parede é {area:.2f}m², e será necessario {tinta:.2f} litro de tinta.')
