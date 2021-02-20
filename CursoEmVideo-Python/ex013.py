# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario_antigo = float(input('Qual o salário atual: R$'))
salario_aumentado = salario_antigo + (salario_antigo * 15 /100)
print(f'O salário antigo era de R${salario_antigo:.2f}, com o aumento de 15% o salário agora será de R${salario_aumentado:.2f}')
