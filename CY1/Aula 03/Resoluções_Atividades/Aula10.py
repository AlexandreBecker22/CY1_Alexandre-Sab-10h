# 1)

class car:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar():
        print("Car is on")
    def infoCar(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, ano de fabricação: {self.ano}')

car.ligar()
carOne = car('VolksWagen','Polo antigo', '2014')
carOne.infoCar()

# 2)

class saldoBancario:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def sacar(self, x):
        self.saldo = int(self.saldo) - x
    def depositar(self, y):
        self.saldo = int(self.saldo) + y
    def info(self):
        print(f'A pessoa {self.titular} possui R${self.saldo} ,00.')

x = int(input('Qual vai ser a quntia sacada?'))
y = int(input('Qual vai ser a quantia depositada?'))

sb1 = saldoBancario('Aluno1', '950')

sb1.sacar(x)
sb1.depositar(y)
sb1.info()
