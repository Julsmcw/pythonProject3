
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму: '))
for keys, value in per_cent.items():
    per_cent[keys] = value * money / 100
    deposit = list(per_cent.values())
i = max(per_cent.values())
print(deposit)
print('Максимальная сумма,которую Вы можете заработать: ', int(i))