pais_A = 80000
pais_B= 200000
count = 1

while pais_A <= pais_B:
    calculo_A = pais_A * 0.3
    calculo_B = pais_B * 0.15
    
    if pais_A <= pais_B:
        print ('Anos ',count, 'habitantes pais A: ', '%.0f' % calculo_A)
        print ('Anos ',count, 'habitantes pais B:', '%.0f' % calculo_B)
        pais_A+=calculo_A
        pais_B+=calculo_B
        count+=1


    else:
        print ('Paises tem a mesma taxa populacional!')

print ('O pais A ultrapassara o pais B em ',count , 'Anos!')
print ('Habitantes pais A: ', '%.0f' % pais_A)
print ('Habitantes pais B: ', '%.0f' % pais_B)