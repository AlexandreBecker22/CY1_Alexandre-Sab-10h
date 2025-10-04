# modulo → arquivo separado que pode ser ter suas funções chamadas em outro arquivo → na mesma pasta: 'import (função/modulo)'                                                            \
#                                                                                    \
#                                                                                     → em outra pasta: forma 1 (somente a função) → 'import (pasta).(função) as (apelido da função/modulo no código)' forma 2 (todo o modulo) → 'from (pasta) import (modulo)              
import math

def soma(a, b):
    return a+b

def subtracao(a, b):
    return a-b

def multiplicacao(a, b):
    return a*b

def divisao(a, b):
    return a/b

def raiz(a):
    return math.sqrt(a)

