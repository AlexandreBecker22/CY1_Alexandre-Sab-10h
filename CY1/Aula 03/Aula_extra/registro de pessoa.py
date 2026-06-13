class Registro_de_pessoas:
    def __init__(self, nome, idade, cpf, mãe, pai):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.mãe = mãe
        self.pai = pai
    def Carteirinha(self):
        print(f"Carteirinha de {self.nome}:\n nome:{self.nome}\n idade:{self.idade}\n cpf:{self.cpf}\n filiação:\n   mãe:{self.mãe};\n   pai:{self.pai}")
    def nova_pessoa(self):
        n = input("Qual é o seu nome?")
        i = input("Qual é o sua idade?")
        c = input("Qual é o seu cpf ?")
        m = input("quem é sua mãe?")
        p = input("quem é sua mãe?")
        NewPerson = Registro_de_pessoas(self,n,i,c,m,p)
        NewPerson.nova_pessoa()
        NewPerson.Carteirinha(self)
       
