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


def collect_Ratings(rating):
    if rating in dic_rating.keys():
        dic_rating[rating] += 1
    else:
        dic_rating[rating] = 1


def collect_Years(years):
    if years in dic_years.keys():
        dic_years[years] += 1
    else:
        dic_years[years] = 1


def write_Ratings(ratings_movies):
    for k, v in dic_rating.items():
        ratings_movies.write(k + " - " + str(v) + " movies" + "\n")


def write_Years(years_movies):
    for k, v in dic_years.items():
        years_movies.write(k + " - " + str(v) + " movies" + "\n")


try:
    readFile = open('src/homework7/ratings.list', 'r')
    lines = readFile.readlines()
    top250_movies = open('src/homework7/out/top250_movies.txt', 'a')
    ratings_movies = open('src/homework7/out/ratings.txt', 'a')
    years_movies = open('src/homework7/out/years.txt', 'a')

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

            collect_Ratings(rating)
            collect_Years(years)

            top250_movies.write(text + "\n")

    write_Ratings(ratings_movies)
    write_Years(years_movies)

except Exception as e:
    print("file error: ", e)
finally:
    readFile.close()
    top250_movies.close()
    ratings_movies.close()
    years_movies.close()
