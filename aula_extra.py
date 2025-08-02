# input -> variavel que o usuario digita

# int-> inteira
# float-> pode ser não inteira

#primeiro-> ' if ' _________ meio-> ' elif ' __________ final-> ' else '

print(" Bem vindo(a) \n Que operação você quer realizar hoje? \n Digite 1 para adição, 2 para subtração, 3 para divisão e 4 para múltiplicação.")

operacao = int(input("Escolha sua operação: "))

num1 = float(input("Qual será o primeiro número? "))
num2 = float(input("E qual será o segundo número? "))

if operacao == 1:
    resultado = num1+num2

elif operacao == 2:
    resultado = num1-num2

elif operacao == 3:
    if num2 == 0:
     print("É impossível resolver está opeção, uma vez que não é possível dividir um número por zero. Por favor reinicie o programa e selecione uma operação válida.")
     resultado = "ERRO"
    else:
     resultado = num1/num2



elif operacao == 4:
    resultado = num1*num2


else:
    print("Essa operação não existe. Por favor reinicie o programa e selecione uma operação disponível.")
    resultado = "ERRO"

print("resultado =")
print(resultado)




