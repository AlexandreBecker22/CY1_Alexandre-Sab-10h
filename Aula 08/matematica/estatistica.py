import inspect as inp

def média():
    a = input("De quantos números a média vai ser calculada? " )
    TotalNum=[]
    for c in range(a):
        num= float(input(f'Digite o {c}º número: '))
        TotalNum.append(num)

    if TotalNum == 0:
        print('ERRO, reinicie o programa')
    else:
        return TotalNum/a
    
def média_ponderada():
    k = input("De quantos números a média vai ser calculada? " )
    Totalnumm=[]
    for c in range(k):
        num= float(input(f'Digite o {c}º número: '))
        peso= float(input(f'Digite o peso do {c}º número: '))
        numm = num*peso
        Totalnumm.append(numm)

    if Totalnumm == 0:
        print('ERRO, reinicie o programa')
    else:
        return Totalnumm/(k+peso)
    
média()
média_ponderada()
