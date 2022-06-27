'''
Checa se número fornecido via console faz parte da sequência
de Fibonacci
'''

def getFibonacci(number):
    fibonacci = [0, 1]
    while fibonacci[-1] < number:
        nextNumber = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(nextNumber)
    return fibonacci

def checkFibonacci(number):
    fibonacci = getFibonacci(number)
    return number in fibonacci


if __name__ == '__main__':
    print('Informe o número desejado: ')
    number = int(input())
    result = checkFibonacci(number)
    if result:
        print(f'O número {number} está contido na sequência.')
    else:
        print(f'O número {number} NÃO faz parte da sequência.')
