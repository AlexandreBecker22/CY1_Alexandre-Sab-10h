# condicionais → São estruturas de codigo que so executam em determinadas circunstâncias

'''
estrutura base de condicional

if condiçao:
    'código'
'''

# Operadores logicos 

'''
== → igualdade | Ex.: (10 == 10 = true) ou (10 == 8 = False)
!= → desigualdade | Ex.: (10 != 9 = true) ou (10 != 10 = False)
> → maior que | Ex.: (10 > 9 = true) ou (10 > 15 = False)
< → menor que | Ex.: (10 < 16 = true) ou (10 < 7 = False)
>= → maior ou igual que | Ex.: (10 >= 2 = true) ou (10 >= 4 = False)
<= → menor ou igual que | Ex.: (10 <= 21 = true) ou (10 <= 11 = False)
'''

# Comparadores logicos 

'''
and (&&) → Retorna verdadeiro se TODOS os resultados forem verdadeiros
or (||) → Retorna verdadeiro se apenas um dos resultados for verdadeiro
not (!) → Ele busca o oposto
'''


nota = float(input('insira a nota do aluno: '))

if nota >= 6:
    print('aluno aprovado com nota: {nota}')
elif nota >= 3:
    print('aluno reprovado com nota :  {nota}')
else: 
    print('aluno de recuperação com nota: {nota}')
