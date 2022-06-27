'''
Reverte string fornecida por usuário via console
'''

def revertString(string):
    reversedString = ''
    for i in range(len(string)):
        reversedString += string[-(i+1)]
    return reversedString


if __name__ == '__main__':
    print(f'Insira string para inversão: ')
    string = str(input())
    print('String invertida: ')
    print(revertString(string))
