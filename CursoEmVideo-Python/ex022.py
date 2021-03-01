# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letra maiúsculas;
# -> O nome com todas as letras minúsculas;
# -> Quantas letras no total(sem considerar espaços).
# -> Quantas letras tem o primeiro nome.
nome = input('Digite o seu nome completo: ').strip()
lista_nome = nome.split()
print(f'O seu nome completo em maiúscula é {nome.upper()}')
print(f'O seu nome completo em minúscula é {nome.lower()}')
nome = nome.replace(' ', '')
print(f'O seu nome completo ao todo tem {len(nome)} letras')
print(f'O seu primeiro nome tem {len(lista_nome[0])} letras')
