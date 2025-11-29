arquivo = open('bloco_de_notas-teste_de_arquivos.txt', 'a')# o 'a' pode mudar conforme o uso, veja abaixo algumas as siglas que podem ser usadas
'''
r - read (retorna o que está escrito)
w - write (reescreve o texto(apaga tudo e escreve o que for 'mandado'))
a - write (adiciona textos ao texto principal(o write sem apagar o que já estava escrito))
r+ - read/write(com 'a')_pode usar tanto 'read' quanto 'write[a]' (read (retorna o que está escrito) e write[a] (reescreve o texto(apaga tudo e escreve o que for 'mandado')))
'''
# Exemplos de uso:

# r:

print(arquivo.read())# a sigla tem que ser 'r' ou 'r+'

# w:

arquivo.write('reeeeeeeeeeeeessscreeeviiiiiiiiiiiiiii')# a sigla tem que ser 'w'  


# a:

arquivo.write('adiciooooooneiiiiiiiii coooisaaaa')# a sigla tem que ser 'a' ou 'r+'

# r+:

'''
pode fazer tanto o 'r' quanto o 'a'
'''
