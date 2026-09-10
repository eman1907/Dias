def calculaDias(d, m, a):
    mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    acum = 0
    for i in range(a - 1):
        if (i % 4) or (i % 100 == 0 and i % 400):
            acum += 365 
        else:
            acum += 366 
    for i in range(m - 1):
        acum += mes[i]
    acum += d
    return acum 

data1 = input('Digite a primeira data no estilo xx/xx/xxxx: ')
data1 = data1.split('/')
dias1 = int(data1[0])
mes1 = int(data1[1])
ano1 = int(data1[2])

data2 = input('Digite a segunda data no estilo xx/xx/xxxx: ')
data2 = data2.split('/') 
dias2 = int(data2[0])
mes2 = int(data2[1])
ano2 = int(data2[2]) 

totalDias1 = calculaDias(dias1, mes1, ano1)
totalDias2 = calculaDias(dias2, mes2, ano2)

dif = totalDias2 - totalDias1
if dif < 0:
    dif *= -1
print('Sao' , dif, 'dias entre as duas datas') 
