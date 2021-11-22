'''
Города
Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите,
в какой стране он находится.
Входные данные
Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с
названия страны, затем идут названия городов этой страны. В следующей строке записано число M,
далее идут M запросов — названия каких-то M городов, перечисленных выше.
Выходные данные
Для каждого из запроса выведите название страны, в котором находится данный город.
Примеры
Входные данные
2
Russia Moscow Petersburg Novgorod Kaluga
Ukraine Kiev Donetsk Odessa
3
Odessa
Moscow
Novgorod
Выходные данные
Ukraine
Russia
Russia
'''


def city_country():
    print("задача 5_2:")
    city_country_map = {}
    list_of_cities = []
    data_list = [['Russia Moscow Petersburg Novgorod Kaluga'], ['Ukraine Kiev Donetsk Odessa']]
    city_list = ['Odessa', 'Moscow', 'Novgorod']
    for item in data_list:
        country, *cities = item[0].split()
        for city in cities:
            city_country_map[city] = country

    for city in city_list:
        list_of_cities.append(city)

    for city in list_of_cities:
        print("Город ", city, "находится в ", city_country_map[city])
