import json
arquivoJ = open('Aula/bloco-teste-texto-json.json','r')
# tem algumas mudanças no 'json', veja abaixo
'''
r - read → load
w - write →
a - write →
r+ - read → load / write(a) →
'''

# exemplos com listas:

dados = json.load(arquivoJ)
alunos = dados['alunos']
notas = []

for aluno in alunos:
    notas.append(aluno['nota'])
# adiciona todas as notas de cada aluno

maior_nota = max(notas)# pega o maior
menor_nota = min(notas)# pega o menor
média = sum(notas)/len(notas)# sum → soma os números da lista // len → conta quantos itens( no caso, números)

print(f'Maior nota da turma: {maior_nota}\nMenor nota da turma: {menor_nota}\nMédia das notas: {média}')
