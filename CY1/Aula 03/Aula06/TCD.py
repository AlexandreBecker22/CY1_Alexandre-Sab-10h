#region Tuplas
'''
 → Tuplas sao 'listas' cujos valores após inserção n podem ser ALTERADOS como por ex uma lista com os dias das semanas.
 → Para criar uma Tupla basta fazer igual uma lista mas invés de {} usamos () e separamos os elements com a ,
'''

print('Tuplas\n')

t = ('Dom','Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab')
print(t)
t = ('Dom','Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Lan')
print(t)

# Na hora de buscar um dado na Tupla em um index especifico usamos [] igual usmos em listas e strings

print(t[2])
print(t[2:5])

# Métodos que funcionam com tuplas 

# len() para retornar o tamanho
print(len[t])

# index() para retornar em qual indice esta o elemento 
print(t.index('Ter'))


#endregion

#region Conjuntos(sets)

print('\nConjuntos Sets\n')

'''
 → Conjuntos Sets  tbm sao listas, mas sao mutaveis. Porem não podem repettir valores iguais( 2 vezes ou mais a mesma coisa)
 → Para criar um conjunto sets basta criar uma variavel que vai receber esse conjunto e apos o sinal de '=' escrever set()
'''

x = set()

# Para adicionar elementos ao conjunto basta usar o metodo add() e como parametro  passar o elemento  que deseja inserir 

x.add(1)# vai funcionar ←-¬
x.add(2)# vai funcionar   |
print(x)#                 /
x.add(1)#não vai funcionar

#endregion

#region Dicionários

'''
→ Um dicionario é uma estrutura de dados que armazena informações em pares, chave-valor. Ele permiti acesso fácil e rapido dos valores pelas suas chaves.

→ Para criar um dicionário, use o simbolo de {} após declarar a variavel. Um dicionario e uma coleçao em chave-valor 
'''
print("\nDicionário \n")

meu_dicionario = {
    'nomme' : 'Pedro',
    'idade' : 27,
    'cidade' : ['Lagoa Santa']
}

'''
→ Acessando valores em um dicionario
'''

# Para acessar um valor, use a chave correspondende

print(meu_dicionario['nome'])
print(meu_dicionario['idade'])
print(meu_dicionario['cidade'])

# Para adicionar um valor em uma chave 
meu_dicionario['cidade'].append('Belo Horizonte')
print(meu_dicionario['cidade'])

#Para adicionar uma chave-valor
meu_dicionario['profissão'] = 'profeessor'
print(meu_dicionario)

#Para modificar o valor de uma chave existente 
meu_dicionario['idade'] = '26'
print(meu_dicionario['idade'])

# Para remover uma chave-valor do dicionario 
del meu_dicionario['cidade']
print(meu_dicionario)

# Iterando sobre um dicionario
# Podemos percorrer todas as chaves-valores do dicionario
for chave in meu_dicionario:
    print(f'Chave: {chave}, Valor: {meu_dicionario[ chave ]}')

#Verificando se uma chavve esta no dicionario 
if 'nome' in meu_dicionario:
    print( 'A chave "nome" está em meu_dicionario.')

# Limpando o dicionario 
meu_dicionario.clear # esse comando eliminara TODAS as chaves-valores do dicionario
print(meu_dicionario)

#endregion