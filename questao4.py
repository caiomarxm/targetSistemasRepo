'''
Calcula percentual por estado no faturamento
'''

invoicing = {
        'SP': 67836.43, 
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

def getTotal(invoicing):
    summation = 0
    for value in invoicing.values():
        summation += value
    return summation

def getPercentual(state):
    return invoicing[state]/getTotal(invoicing)

if __name__ == '__main__':
    
    total = getTotal(invoicing)
    print('Para qual estado deseja calcular o percentual?')
    print('Obs.: Inserir sigla (Exemplo: "SP" para São Paulo)')
    state = input().upper()

    try:
        percentual = getPercentual(state)
        print(f'{state} representa {percentual*100:.2f}% do faturamento mensal.')
    except:
        print('Não há informações suficientes para concluir requisição.')
        print('Estados disponíveis: SP, RJ, MG e ES')
