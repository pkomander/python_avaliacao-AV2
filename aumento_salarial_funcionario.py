def novosalario(salario, count, novo_salario):
    print ('Em ', count, 'recebeu de salario: R$', '%.2f' % novo_salario)





count = 1995
salario = 1000
em_96 = 0.15
em_97 = 0.3

print('Em 1995 recebeu o salario: R$ 1000')

salario = float(input('Digite o seu salario em 1995: '))

while count < 1996:
    salario = 1000 * em_96
    novo_salario = 1000 + salario
    count+=1
    print('Em ', count, 'recebeu de salario: R$', novo_salario)
    break


while count < 2020:
    if novo_salario >= 1000:
        novo_salario+= (novo_salario * em_97)
        em_97*=2
        count+=1
        #print ('Em ', count, 'recebeu:', novo_salario)

        novosalario(salario, count, novo_salario)


'''while count < 2020:
    salario = 1000 * em_96
    novo_salario = 1000 + salario
    #print('Em ', count, novo_salario)

    if novo_salario >= 1000:
        novo_salario+= (novo_salario * em_97)
        em_97*=2
        count+=1
        #print ('Em ', count, 'recebeu:', novo_salario)

        novosalario(salario, count, novo_salario)'''

