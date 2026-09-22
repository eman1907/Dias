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

# Datas fixas só para teste (sem input)
dias1, mes1, ano1 = 10, 5, 2024
dias2, mes2, ano2 = 20, 8, 2024

totalDias1 = calculaDias(dias1, mes1, ano1)
totalDias2 = calculaDias(dias2, mes2, ano2)

dif = totalDias2 - totalDias1
if dif < 0:
    dif *= -1

print('Sao', dif, 'dias entre as duas datas')