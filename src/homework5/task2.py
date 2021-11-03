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
    cityCountryMap = {}
    listOfCities = []
    for _ in range(int(input('Ведите число: '))):
        country, *cities = input('Введите страну и ее города: ').split()
        for city in cities:
            cityCountryMap[city] = country

    for _ in range(int(input('Ведите число: '))):
        city = str(input('Введите город: '))
        listOfCities.append(city)
        print()

    for city in listOfCities:
        print(cityCountryMap[city])


if __name__ == "__main__":
    main()
