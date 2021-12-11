'''
В файле хранятся данные с сайта IMDB. Скопированные данные хранятся в файле
./data_hw5/ ratings.list.
Откройте и прочитайте файл(если его нет необходимо вывести ошибку).
Найдите ТОП250 фильмов и извлеките заголовки.
Программа создает 3 файла  top250_movies.txt – названия файлов, ratings.txt – гистограмма
рейтингов, years.txt – гистограмма годов.
'''


import re


dic_rating = {}
dic_years = {}
lines_top250 = ''


def collect_ratings(rating):
    '''Собирает рейтинги в словарь'''
    if rating in dic_rating.keys():
        dic_rating[rating] += 1
    else:
        dic_rating[rating] = 1


def collect_years(years):
    '''Собирает годы выпуска в слоаврь'''
    if years in dic_years.keys():
        dic_years[years] += 1
    else:
        dic_years[years] = 1


def write_ratings():
    '''Записывает рейтинги'''
    with open('src/homework7/out/ratings.txt', 'a') as file_ratings_movies:
        for k, v in dic_rating.items():
            file_ratings_movies.write(k + " - " + str(v) + " movies" + "\n")


def write_years():
    '''Записывает годы выпуска'''
    with open('src/homework7/out/years.txt', 'a') as file_years_movies:
        for k, v in dic_years.items():
            file_years_movies.write(k + " - " + str(v) + " movies" + "\n")


def write_top250():
    '''Записывает топ-250'''
    with open('src/homework7/out/top250_movies.txt', 'a') as file_top250_movies:
        file_top250_movies.write(lines_top250)


try:
    with open('src/homework7/ratings.list', 'r') as readFile:
        lines = readFile.readlines()
    count = 0
    pattern = re.compile(r"([0-9]\.[0-9])([0-9,:?!\- a-zA-Z.�пїЅ']+)(\([0-9\/I]{4,6}\))")
    for item in lines:
        if count == 250:
            break
        if len(re.findall(pattern, item)) != 0:
            result = re.findall(pattern, item)
            text = result[0][1].strip()
            rating = result[0][0].strip()
            years = result[0][2].replace('(', '').replace(')', '')
            count += 1

            collect_ratings(rating)
            collect_years(years)
            lines_top250 += text + "\n"

    write_top250()
    write_ratings()
    write_years()

except Exception as e:
    print("file error: ", e)
