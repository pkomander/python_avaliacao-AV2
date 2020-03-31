count = 10
n = int(input('Digite um numero: '))
while count < n:
    divisao = count / 10
    if divisao < n:
        print(count)
        count+=10