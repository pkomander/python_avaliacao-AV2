#logica soma dos numeros pares
print ('A soma de todos os numeros pares entre 2 e 100 -> 1')
print ('A soma de todos os quadrados entre 1 e 100 -> 2')
print ('A soma de todos os numeros impares entre A e B -> 3')
print ('A soma de todos os digitos impares de n -> 4')

pergunta = int(input('Digite a opcao: '))


if pergunta == 1:
    print('Os numeros pares são: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98  100')
    #num = int(input('digite os numeros pares de 2 ate 100: '))
    media = 0
    num = 2
    count = 1
    while count < 50:
        media+= num
        count+=1
        print("A soma dos numeros pares de 2 ate 100: ",media)



#a soma dos quadrados
if pergunta == 2:
    soma = 0
    count = 1
    while count <= 100:
        soma+= (count * count)
        print (soma)
        count+=1
    print("A soma dos quadrados de 1 ate 100 e: ",soma)


#a soma de todos os numeros impares entre a e b
if pergunta == 3:
    count = 0

    print ('Somente numeros de 0 a 9')

    while count == 0:
        num1 = int(input('Digite um numero: '))
        num2 = int(input('Digite outro numero: '))
        if (num1 % 2 != 0) and (num2 % 2 != 0):
            soma = num1 + num2
            print (soma)
            count+=1
            break

        elif (num1 % 2 == 0) and (num2 % 2 == 0):
            print ('Todos os numeros sao par, digite novamente')

        elif (num1 % 2 != 0) and (num2 % 2 == 0):
            soma = num1
            print (soma)
            break

        elif (num1 % 2 == 0) and (num2 % 2 != 0):
            soma = num2
            print (soma)
            break

#a soma de todos os numeros impares de n
if pergunta == 4:
    posicao = 0

    num = (input('Digite um numero: '))
    fim = len(num)
    soma = 0

    while posicao <= fim:
        if int(num[posicao]) % 2 != 0:
            soma+= int(num[posicao])
        posicao+=1
        print (soma)

        elif number % 2 == 0:
            print ('Todos os numeros sao par')
            break
