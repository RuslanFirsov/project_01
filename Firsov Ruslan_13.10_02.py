# Задача 2
# Есть словарь координат городов sites,
# Составьте словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2


sites = {
    'Москва': (550, 370),
    'Лондон': (510, 510),
    'Париж': (480, 480),
}
distances_Moscow = {}
moscow_to_paris = (sites['Москва'][0] - sites['Лондон'][0]) ** 2 + (sites['Москва'][1] - sites['Лондон'][1]) ** 2
moscow_to_london = (sites['Москва'][0] - sites['Париж'][0]) ** 2 + (sites['Москва'][1] - sites['Париж'][1]) ** 2


distances_Moscow['Москва'] = {
    'Лондон': moscow_to_london,
    'Париж': moscow_to_paris,
    }


distances_London = {}
london_to_paris = (sites['Лондон'][0] - sites['Париж'][0]) ** 2 + (sites['Лондон'][1] - sites['Париж'][1]) ** 2
london_to_moscow = (sites['Лондон'][0] - sites['Москва'][0]) ** 2 + (sites['Лондон'][1] - sites['Москва'][1]) ** 2

distances_London['Лондон'] = {
    'Париж': london_to_paris,
    'Москва': london_to_moscow
}


distances_Paris = {}
paris_to_moscow = (sites['Париж'][0] - sites['Москва'][0]) ** 2 + (sites['Париж'][1] - sites['Москва'][1]) ** 2
paris_to_london = (sites['Париж'][0] - sites['Лондон'][0]) ** 2 + (sites['Париж'][1] - sites['Париж'][1]) ** 2

distances_Paris['Париж'] = {
    'Москва': paris_to_moscow,
    'Лондон': paris_to_london
}

print(f' {distances_Moscow},\n {distances_Paris},\n {distances_London}')
