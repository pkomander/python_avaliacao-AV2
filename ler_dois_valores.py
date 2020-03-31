x = 1

while x == 1:
    num1 = float(input('Digite um numero: '))
    num2 = float(input('Digite outro numero: '))

    soma = num1 + num2
    print('O resultado da soma e de ', '%.0f' % soma)

    pergunta = int(input('Novo calculo (S -> 1 / N -> 2): '))

    if pergunta == 1:
        x = 1

    else:
        print ('Fim do codigo')
        x+= 2
