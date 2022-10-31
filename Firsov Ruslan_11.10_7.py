# Задача 3
# Есть словарь списков количества товаров на складе.
# Рассчитать на какую сумму лежит каждого товара на складе
# Вывести стоимость каждого товара на складе: один раз распечатать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678'
}
# Есть словарь списков количества товаров на складе.

store = {
    '12345': [{'quantity': 27, 'price': 42},],
    '23456': [{'quantity': 22, 'price': 510},{'quantity': 32, 'price': 520},],
    '34567': [{'quantity': 2, 'price': 1200},{'quantity': 1, 'price': 1150},],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
try:
    user_input = input(f'Введите искомый товар из списка\n{list(goods)}: ')
    search_res = goods[user_input]
    ind = 0
    quantity = 0
    price = 0
    for dic in store[search_res]:
        quantity += store[search_res][ind]['quantity']
        price += store[search_res][ind]['price']
        ind += 1
    print(f'{user_input} - количество: {quantity}, стоимость: {price}')
except KeyError:
    print('Введите наименование товара из списка!')


#  О! Отлично!
