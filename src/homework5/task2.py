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


def main():
    city_country_map = {}
    list_of_cities = []
    for _ in range(int(input('Ведите количество стран: '))):
        country, *cities = input('Введите страну и ее города: ').split()
        for city in cities:
            city_country_map[city] = country

    for _ in range(int(input('Ведите количество городов для проверки: '))):
        city = str(input('Введите город: '))
        list_of_cities.append(city)

    for city in list_of_cities:
        print("Город", city, "находитя в стране", city_country_map[city])


if __name__ == "__main__":
    main()
