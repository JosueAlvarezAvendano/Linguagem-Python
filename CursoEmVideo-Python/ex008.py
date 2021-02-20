# Escreva um programa que leia um valor em metros e o exiba conertido em centimetros e milimetros.
metro = float(input('Digite um valor em metros: '))
centimetro = metro * 100
milimetro = metro * 1000
print(f'O valor de {metro}m convertido para centimtro é igual a {centimetro:.2f}cm.')
print(f'O valor de {metro}m convertido para milimetro é igual a {milimetro:.2f}mm.')
