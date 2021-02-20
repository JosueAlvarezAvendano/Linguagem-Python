# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco_normal = float(input('Qual o preço do produto: R$'))
preco_desconto = preco_normal *0.95
print(f'O preço do produto é R${preco_normal:.2f}, na promoção com 5% de desconto o produto saira por R${preco_desconto:.2f}')
