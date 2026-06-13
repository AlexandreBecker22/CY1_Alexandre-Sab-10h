'''
1)
'''
name = input("Qual é seu nome?")
age = int(input("E qual é sua idade?"))
future_age = age + 5
print(f"Olá {name}! Daqui a 5 anos vc terá {future_age}.")

'''
2)
'''
n = int(input('Qual foi sua nota?'))
if(n >= 7):
    print('Aluno aceito!')

elif(n < 7 and n > 6):
    print('Aluno passa se sobrar vaga, se não vai para a recuperação.')

elif(n < 6 and n > 4) :
    print('Aluno de recuperação final.')

else:
    print('Que pena. O aluno tomou bomba!')


'''
3)
'''

