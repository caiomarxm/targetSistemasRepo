import json

def getMax(content):
    maximum = 0
    day = 0
    for element in content:
        currentValue = element['valor']
        if maximum < currentValue:
            maximum = currentValue
            day = element['dia']
    return day, maximum

def getMin(content):
    minimum = content[0]['valor']
    for element in content:
        currentValue = element['valor']
        if minimum > currentValue:
            minimum = currentValue
    return minimum

def getMean(content):
    summation = 0
    counter = 0
    for element in content:
        currentValue = element['valor']
        summation += currentValue
        if currentValue != 0:
            counter += 1
    meanValue = summation/counter
    return meanValue

def countAboveMean(content):
    mean = getMean(content)
    counter = 0
    for element in content:
        currentValue = element['valor']
        if currentValue > mean:
            counter += 1
    return counter



if __name__ == '__main__':
    with open('dados.json') as file:
        content = json.load(file)
        maximumDay, maximum = getMax(content)
        minimum = getMin(content)
        daysAboveMean = countAboveMean(content)
    print(f'Faturamento máximo de R${maximum:.2f} atingido no dia {maximumDay}.')
    print(f'Faturamento mínimo de R${minimum:.2f}.')
    print(f'Dias acima da média: {daysAboveMean}')
