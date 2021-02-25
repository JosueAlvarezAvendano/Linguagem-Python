# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.
print('=' * 18)
print('ALUGUEL DE CARROS')
print('=' * 18)
dias = int(input('Por quantos dias foi alugado: '))
km = float(input('Quantos Km foi rodado: '))
total = dias * 60 + km * 0.15
print(f'O total a pagar pelo carro alugado será de R${total:.2f}')
