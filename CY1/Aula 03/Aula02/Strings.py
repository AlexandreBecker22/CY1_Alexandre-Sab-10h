# char → salva um único carectere.
# char[] → lista de caracteres, que podem formar palavras e frases.

# 'variavel'[] → lista de informações (salvas na variavel).


# Strings é um tipo de variável que armazena textos. Para utilizar uma string basta declarar uma variável e passar como valor o texto que deseja salvar entre '' ou ""

texto = 'Ctrl+Play-  Escola de Programação e Robótica'

# Strings não nescessáriamente precisam estar atreladas à uma variável, no caso da exebição através da função print()

print(texto)
print('Texto impresso direto do print')

# Para saltar linhas durante a exibição de um texto se utiliza o comando '\n'

print('Saltando \n\n linhas \n !')

print('Olá\n\nlinhas\n!')

# Para dar um espaçamento entre palavras equivalente a tecla 'tab' pode-se usar o comando '\t'

print('Teste\tde\tespaçamento')

# Caso você saber qual o tamanho de uma string em relação à quantidade de caracteres basta usar a função len() passando como parâmetro a string que deseja saber a informação.

print(len(texto))

# Em uma string podemos usar o Index para utilizar apenas parte de uma string para exibições, comparações etc. Para trabalhar com Index basta após chamar a variável onde a string está salva usar o comando de '[]'

nome = 'Pedro Paulo Sousa do Couto'

print(nome[0]) # Será imprimido apenas a primeira letra da string 'P'

# A partir de um caractere

print(nome[6:]) # Paulo Sousa do Couto

# Até um caractere

print(nome[:6]) # Pedro

# De um ponto ao outro

print(nome[12:17]) # Sousa

# usando números negativos no [] fazemos a manipulação inversa do index

print(nome[-1]) # o

#Tudo até o -6
print(nome[:-6]) # Pedro Paulo Sousa do

# Para ir saltenado de caractere a caractere na quantidade desejada
print(nome[::2])# PdoPuoSuad ot

# strings são imutáveis, ou seja, não para mudar só uma parte dele com a função index. Para mudar a string vc tem que muda-la completamente.

'''
NÃO PODE
nome[0] = F

PODE
nome = "Fedro Paulo Sousa do Couto"

'''

# É possível "somar" uma string a outra, ou seja, concatenação

nome2 = 'Frederico'
sobrenome2 = ' Cunha'

print(nome2+sobrenome2)
# É possível repetir uma string várias vezes 

print((nome2+sobrenome2+' ')*10)

# Para unir letras com numeros, usamos a função 'str()', que converte qualquer tipo de variável em string.(e para transformar variáveis em se usa 'int()').

numeroDeIrmãos = 2
print('Você tem dois '+str(numeroDeIrmãos)+' irmãos')

# Outra forma de fazer isso é usar a vírgula ( que separa os itens).

print('Você tem dois ', numeroDeIrmãos, ' irmãos')

