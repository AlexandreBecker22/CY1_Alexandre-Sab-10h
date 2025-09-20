#Funções

'''
Funções são criadas com o intuito de exectar uma cadeia de comandos que podem/vão ser repetir várias vezes no programa, assim facilitando a programação (simplificando o caomando)
'''

# Para criar uma função basta usar o 'def', escrever o nome da função seguida por(), e finalizr a linha com ':'. EX.: def Pular():

#Dica Tente stabelecer padrões para diferenciar funções de variaveis

def Boas_vindas():
    print('Boas-Vindas!!!')

# Para executar uma função basta chama-la da seguinte forma

Boas_vindas()

# As vezes podem ter informações dentro dos '()', que sao parametros para comandos que necessitam deles

def ola(nome):
    print(f'Olá {nome}!!')

ola('Alê')

def velocidade(distância, tempo=1.5):
    if