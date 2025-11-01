#fazer testes ao longo da programaçao, para nao ter que ficar procurando depois
# Exemplo de teste:

def soma(a, b):
    return a + b

def teste_de_soma():
    assert soma(4, 6) == 10
    assert soma(2, 6) == 8
    assert soma(-57, 58) == 1

try:
    teste_de_soma()
    print("Tudo Ok")
except AssertionError:
    print("Algum teste falhou")

# Ativ: Crie uma fução com a e b e a teste

def multiplicação(a,b):
    return a*b

multiplicação(9, 5)

def teste_de_mult():
    assert multiplicação(9, 2) == 18
    assert multiplicação(5, 4) == 20
    assert multiplicação(8, 0) == 0

try:
    teste_de_mult()
    print("Tudo Ok")
except AssertionError:
    print("Algum teste falhou")

class saldoBancario:
    def __init__(self, dono, saldo):
        self.dono = dono
        self.saldo = saldo
    def depositar(self, Val_Dep):
        self.saldo += Val_Dep
    def sacar(self, Val_Sac):
        if Val_Sac > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= Val_Sac

def teste_contas():
    conta = saldoBancario("Xaveco", 3)

    conta.depositar(2)
    assert conta.saldo == 5

    conta.sacar(4)
    assert conta.saldo == 1

    try:
        conta.sacar(1)
    except ValueError:
        print('Erro de saque passou')

teste_contas()

