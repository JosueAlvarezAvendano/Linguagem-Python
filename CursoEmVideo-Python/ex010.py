# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Dados: dolar = 5.38  (20/02/2021)
real = float(input('Quantos reais você tem na carteira: R$'))
dolar = real / 5.38
print(f'Com R${real:.2f} você pode comprar ${dolar:.2f}')
