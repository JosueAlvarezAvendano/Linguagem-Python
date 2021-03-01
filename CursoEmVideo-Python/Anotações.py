''' TIPOS PRIMITIVOS '''
# int -> Números Inteiros (ex.: 7, -4, 0 e 9875)
# floot -> Números Reais (ex.: 4.5, 0.076, -15.223 e 7.0)
# bool -> Valores Logicos (ex.: True e False)
# str -> Valores Caracteres ('Olá', '7.5', ' ')

'''OPERADORES ARITMÉTICOS'''
# + -> adição
# - -> Subtração
# * -> Multiplicação
# / -> Divição
# ** -> Potência
# // -> Divisão Inteira
# % -> Resto da Divisão

'''ORDEM DE PRECEDÊNCIA'''
# 1º -> ()
# 2° -> **
# 3º -> *, /, // e %
# 4º -> + e -

''' FUNÇÕES USUAIS '''
# print('Texto') -> Mostra na tela o que está entre aspas
# input('pergunta') -> Pede alguma coisa para o usuario
# pow(base, expoente) -> Serve para realizar contas de potência

'''METODOS DE TIPOS'''
# type(NomeDaVariavel) -> Mostra o tipo primitivo da variável
# NomeDaVariavel.isnumeric() -> Para saber se a variavel pode ser numérico
# NomeDaVariavel.isalpha() -> Para saber se a variavel pode ser alfabetico
# NomeDaVariavel.isalnum() -> Para saber se a variavel pode ser nalfanumerico
# NomeDaVariavel.isupper() -> Para saber se a variavel está somente em maiuscula
# NomeDaVariavel.islower() -> Para saber se a variavel está somente em minuscula
# NomeDaVariavel.isprintable() -> Para saber se a variavel pode ser impressa na tela
# NomeDaVariavel.isspace() -> Para saber se a variavel é espaço
# NomeDaVariavel.istitle() -> Para saber se a variavel está capitalizada (A 1º letra em maiuscula)

'''FORMATAÇÃO DO PRINT()'''
Nome = 'Oi'
print(f'{Nome:10}!') # Coloca o texto em 10 espaços
print(f'{Nome:<10}!') # Coloca o texto em 10 espaços alinahdo a esquerda
print(f'{Nome:>10}!') # Coloca o texto em 10 espaços alinahdo a direita
print(f'{Nome:^10}!') # Coloca o texto em 10 espaços centralizado
print(f'{Nome:=^10}!') # Coloca o texto em 10 espaços centralizado completado com o que estiver antes
divisao = 4 / 3
print(f'{divisao}') # Mostra o valor total
print(f'{divisao:.1f}') #Mostra até uma casa depois da virgula
print(f'{divisao:.2f}') # Mostra até duas casa depois da virgula
print('Olá, seja bem vindo ao mundo da programação', end=' ') # Se usa para colocar dois prints na mesma linha
print('da linguagem Python.\nEste mundo é incrivel.') # Se usa para colocar uma parte do texto em outra linha

''' MODULOS '''
# Para importar modulos, é necessario realizar o seguinte comando:
# import NomeDoModulo
# Para importar apenas uma função de algum modulo, realizar o seguinte comando:
# From NomeDoModulo import NomeDaFunção, NomeDeOutraFunção
# Funções que já vem com o Python:
# - math (matemática)

# Modulo math:
# ceil -> Está função realiza um arredondamento para cima
# floor -> Está função realiza um arredondamento para baixo
# trunc -> Está função realiza um corte da parte decimal do número
# pow -> Está função realiza uma potência
# sqrt -> Está função realiza uma raiz quadrada
# factorial -> Está função realiza o fatorial

# Modulo random:
# random -> Está função gera um número aleatorio entre 0 e 1
# ranint (1, 10) -> Está função gera um número aleatorio entre 1 e 10
# choise -> Está função escolhe aleatoriamente algo de uma lista criada (A lista inicia no zero)
# sufle -> Está função embaralha uma alista criada (A lista inicia no zero)
