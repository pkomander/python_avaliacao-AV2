def quadradosmenores(count, n, quadrado):
    print ('Os quadrados menores que N: ',quadrado)


#Todos os quadrados menores que n. Por exemplo, se n for 100, imprimir 0 1 4 9 16 25 36 49 64 81.
count = 0
n = int(input('Digite um numero: '))
while count < n:
    quadrado = count * count
    if quadrado < n:
        #print(quadrado)
        count += 1
        quadradosmenores(count, n, quadrado)
