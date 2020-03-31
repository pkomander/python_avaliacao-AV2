soma = 0
compras = 1
while compras > 0:
    compras = float(input('Digite o valor do produtos: '))
    soma+= compras

    if compras == 0:
        print ('Total: ', soma)
        pagamento = float(input('Digite o valor de pagamento: '))
        troco = pagamento - soma
        print('Total: R$', soma)
        print ('Pago pelo cliente: R$', pagamento)
        print ('Troco: R$', troco)
        if troco > 0:
            compras+=1
