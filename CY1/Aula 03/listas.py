# Lista é uma forma de salvar informações em um unico lugar  ou seja varios dados numa unica variavel

# As mesmas regras de declaração de variaveis se aplicam a listas

# O [] é o simbolo que representa lista

convidados = ['Anônimo', 'Jubileu', 'Fulano', 'Fulaninho', 'Zé Não Sei das Quantas', 'Beltrano']
print(convidados)

print('\nPrimeiro convidado da festa de anivessário do Beltrano: '+convidados[0])

# Diferente das strings  as listas sao mutaveis 

convidados[-2]= 'Aquele Lá'
print(convidados)

# uma das formas de adicionar elementos na lista é através da função append() e passar como parametrp para inserir o item(no FINAL da lista).

convidados.append('Aleatório') 
print(convidados)

# Já o comando insert() nos permite escolher o local onde ela vai entrar

convidados.insert(4,'Zé Não Sei das Quantas')
print(convidados)

# para remover um elemento, podemos usar 'del', ...

del convidados[-1]
print(convidados)

#..., 'pop()'( ele remove da liste e salva em outra variavel)...

convidadoremovido = convidados.pop(-2)
print(convidados)
print(convidadoremovido+' foi expulso da festa por pouca aleatoriedade.')

#..., 'remove()' ( ele elimina o elemento da lista através de uma busca)

viajando = 'Fulano'

convidados.remove(viajando)
print(convidados)

# Voltas...
print('Anônimo'+' foi readmitido por um erro.') 
print('Jubileu'+' foi perdoado e readmitido por fazer aleatoriedades na praça pública.')
print('Fulano'+' perdeu o voo e foi readmitido para ser consolado.')

convidados.append('Anônimo'+','+' '+ 'Jubileu'+','+' '+'Fulano')
print(convidados)

# O Reverse() exibi a lista de tras pra frente

print(convidados)
convidados.reverse()
print(convidados)

# Matrizes → são listas que contem listas

timesXpessoas = [["Atlético","Cruzeiro","América","Pouso Alegre"],
                 ["Alezandre","Frederico","Davi","Felipe"]]

print(timesXpessoas[0][1])
print(timesXpessoas[1][1])