# Задача 7
# Есть словарь кодов товаров

titles = {
    'Кроссовки тип 3 - Adidas': '100000110',
    'Мячик тип 2 - Adidas': '100000146',
    'Кепка тип 1 - Adidas': '100000149',
    'Ремень тип 2 - Nike': '100000194',
    'Футболка тип 1 - Adidas': '100000224',
    'Шапка тип 5 - Puma': '100000280',
}
#  Есть словарь списков словарей количества товаров на складе.
sales = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ],
}
# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе c помощью циклов
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

codes = dict((v, k) for k, v in titles.items())


def get_amount(sales_data):
    total_quantity = 0
    total_price = 0
    for elem in sales_data:
        quantity = elem.get('quantity', 0)
        total_quantity += quantity
        total_price += quantity * elem.get('price', 0)
    return {'total_quantity': total_quantity, 'total_price': total_price}


def result(data): # входное значение sales
    return {k: get_amount(v) for k, v in sales.items()}


for k, v in result(sales).items():
    print(f"{codes.get(k)} - {v.get('total_quantity')} шт, стоимость {v.get('total_price')} руб")


