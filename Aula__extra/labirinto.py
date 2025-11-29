'Atividade: '

import random
dado = random.randint(1,6)

def jogo():
    print('Bem-vindo ao jogo "Labirinto"!')
    print('Você é um explorador de labirinto, você vai explorar uma caverna e fazer escolhas no caminho.')
    c1 = input('O tunel se bifurcou, você quer ir para o tunel escuro(1) ou o mais claro(2)?(responda 1 ou 2)')
    print( 'você escolheu a opção', c1)
    if c1 == "1":
        caminho_escuro()
    elif c1 == "2":
        caminho_claro()
    else:
        print('Você escolheu uma opção inválida, por favor reinicie o programa.')
        

def caminho_claro():
        print('Você entrou no tunel mais claro com sucesso!')
        porta = input('pergunta de lógica: qual é o tamanho da porta com 1 metro de largura e 1.6 de altura?')
        if porta == '1.6':
            print('Você acertou!')
            vitória()
        else:
             print('Você errou, boa sorte da próxima vez!')
             derrota()

def caminho_escuro():
    print('Você entrou no tunel escuro com sucesso!')
    print('A visibilidade é pouca e você não consegue enxergar e tem que acertar a porta.(50% de chance para errar e acertar/pura sorte)')
    d1 = dado
    if dado <= 3:
        print('Você é incrivel! Você acertou!')
        vitória()
    else:
            print('Não dava pra ver, não se culpe pelo erro.')
            derrota()


def vitória():
     print('Parabéns você achou uma saída!|Vitória||Se quiser jogar novamente basta reiniciar o programa|')

def derrota():
     print('Desculpe, você falhou.Mais sorte da próxima vez!|Derrota||Por favor reinicie o programa|')


if __name__ == "__main__":  # 'toda vez que o programa iniciar ele vai:'
    jogo()

    