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
    percentual = {
        'SP': 0, 
        'RJ': 0,
        'MG': 0,
        'ES': 0,
        'Outros': 0
    }

    for state in percentual:
        percentual[state] = getPercentual(state)
        print(f'{state} representa {100*percentual[state]:.2f}% do total.')
