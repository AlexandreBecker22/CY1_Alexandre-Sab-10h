import inspect as inp

def média4():
    a = input("De quantos números a média vai ser calculada? " )
    TotalNum=[]
    for c in range(a):
        num= float(input(f'Digite o {c}º número: '))
        TotalNum.append(num)

    if TotalNum == 0:
        print('ERRO, reinicie o programa')
    else:
        return TotalNum/a
    
def