# Поиск самых высокооплачиваемых работников с помощью спискового включения

# нужно найти всех сотрудников, 
# зарабатывающих по крайней мере 100 000 долларов в год

employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,
    'Frank' : 88123,
    'Eve' : 93121}

sum_total = []
for k, v in employees.items():
    if v >= 100000:
        sum_total.append(k)
print(f'Сотрудниками, зарабатывающими 100000 и более являются: {", ".join(sum_total)}.')

