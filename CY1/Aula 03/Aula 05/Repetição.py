# FOR 

'''
for 'item' in 'lista':
     código que vai se repetir

Ex:
for num in lita:
    print(num)
'''

numeros = [1,2,3,4,5,6,7,8,9]

for num in numeros:
    print (num)

jogos = { 'God of War', 'Spider-man', 'Shadows of Mordor', 'MarioKart', 'Pokémon Go'}

for aleatorio in jogos:
    print(aleatorio)

# RANGE → 
for num in range(1, 20):
    print(num)

# especial → separação → Ex: numeros pares

for numero in range(1,15):
    if((numero % 2) == 0):
        print(numero)

# especial → o range só abrange numeros inteiros mas o FOR sim → Ex:

print('Selecione o valor a pagar:')
for exemplo in range(1,50):
    print(f'R$ {exemplo},00')

# WHILE

'''
while condição:
    Código que será repetido
    enquanto a condição for 
    verdadeira.
'''

contador = 1
while contador < 10:
    print("contado:", contador)
    contador += 1

senha = ' '
while senha != '5221':
    senha = input('qual é a senha:')
print('acesso liberado')

soma = 0
numeros = range(1, 101)
i = 0
while soma < 200:
    soma += numeros[i]
    i+=1
print(soma)

# controlando loops com break, continue e pass

'''
do:
    codigo q vai repetir 
while condição de parada
*do while n existe no python ainda

while condição:
    codigo
    if teste1:
        break
    if teste2:
        continue
    else:
        pass
'''

for i in range(1,11):
    if i == 3:
        continue

    if i == 5:
        print("Encontrado o número 5, parando loop(break)")
        break

    if i == 2:
        pass

    print(f'Número atual: {i}')