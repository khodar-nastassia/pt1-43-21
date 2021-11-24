import re


def count_total_price():
    '''Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена, а также

    количество S товара Посчитайте общую цену в рублях и копейках за L товаров.
    Пример:
    Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
    Output: Общая цена 9 рублей 60 копеек
    '''
    print("задача 2_1:")
    M = 3
    N = 20
    S = 3
    coins = (100 * M) + N
    rub = (coins * S) // 100
    cop = (coins * S) % 100
    print("Общая цена: ", str(rub) + " рублей " + str(cop) + " копеек")


def find_longest_word():
    '''Найти самое длинное слово в введенном предложении.

    Учтите что в предложении есть знаки препинания.
    Подсказки:
    - my_string.split([chars]) возвращает список строк.
    - len(list) - количество элементов в списке
    '''
    print("задача 2_2:")
    input_text = "Учтите, что в предложении! есть знаки препинания."
    without_symbols = re.sub(r'[;,.!?]', '', input_text)
    print(without_symbols)
    words = without_symbols.split()
    print("Самое длинное слово: ", max(words, key=len))


def remove_extra_symbols():
    '''Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.

    Например, если было введено "abc cde def", то должно быть выведено "abcdef".
    '''
    print("задача 2_3:")
    string = "abc cde def"
    str_without_space = string.replace(' ', '')
    result = "".join(dict.fromkeys(str_without_space))
    print("Строка без пробелов и повторяющихся букв: " + result)


def count_upper_lowercase():
    '''Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.

    Учитывать только английские буквы.
    '''
    print("задача 2_4:")
    string = "AgUjklT"
    result = re.match(r'[aA-zZ]+', string).group()
    count_small_letter = 0
    for c in result:
        if c.islower():
            count_small_letter = count_small_letter + 1
    count_big_letter = len(result) - count_small_letter
    print("Количество строчных букв: " + str(count_small_letter))
    print("Количество прописных букв: " + str(count_big_letter))


def fibo():
    '''Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы

    и условные операторы. n - вводится
    '''
    print("задача 2_5:")
    n = "5"
    n = int(n)
    fib1 = 0
    fib2 = 1
    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    print("Значение 5-го элемента:", fib2)


def number_polindrom():
    '''Определите, является ли число палиндромом

    (читается слева направо и справа налево одинаково).Число положительное целое,
    произвольной длины. Задача требует работать только с числами
    (без конвертации числа в строку или что-нибудь еще)
    '''
    print("задача 2_6:")
    n = 121
    tmp = n
    reverse_num = 0
    while(n > 0):
        digit = n % 10
        reverse_num = reverse_num * 10 + digit
        n //= 10
    if (tmp == reverse_num):
        print(tmp, "-полиндром")
    else:
        print(tmp, "-не полиндром")


def area_of_triangle():
    '''Даны: три стороны треугольника.Требуется: проверить,

    действительно ли это стороны треугольника.
    Если стороны определяют треугольник, найти его площадь.
    Если нет, вывести сообщение о неверных данных.
    '''
    print("задача 2_7:")
    a = 5.0
    b = 6.0
    c = 3.0
    if (a + b < c and a + c < b and b + c < a):
        print('Неверные данные')
    else:
        p = float((a + b + c) / 2)
        num = float(p * (p - a) * (p - b) * (p - c))
        S = float(num ** 0.5)
        print("Площадь треугольника: ", float(S))


def split_and_join():
    '''You are given a string.

    Split the string on a " " (space) delimiter and join using a - hyphen.
    '''
    print("задача 2_81:")
    line = "You are given a string"
    a = line.split(" ")
    a = "-".join(a)
    print(a)


def swap_cases():
    '''You are given a string and your task is to swap cases. In other words,

    convert all lowercase
    letters to uppercase letters and vice versa.
    For Example:Www.HackerRank.com → wWW.hACKERrANK.COM
    Pythonist 2 → pYTHONIST 2
    '''
    print("задача 2_82:")
    text = 'HackerRank.com presents "Pythonist 2".'
    text2 = text.swapcase()
    print(text2)


def square_number():
    '''Task:The provided code stub reads and integer, n  , from STDIN.

    For all non-negative integers
    i<n, print i^2. Example: n=3
    The list of non-negative integers that are less than  n=3 is [0,1,2].
    Print the square of each number on a separate line.
    0
    1
    4
    '''
    print("задача 2_83:")
    n = 5
    for i in range(n):
        print("Квадрат числа ", i, "=", i * i)


def pairs_of_letter():
    '''Complete the solution so that it splits the string into pairs of two characters.

    If the string contains an odd number of characters then it should replace the missing
    second character of the final pair with an underscore ('_').
    '''
    print("задача 2_84:")
    line = "sjyii"
    if len(line) % 2:
        line += '_'
    print("Пары букв: ", [line[i:i + 2] for i in range(0, len(line), 2)])


def regex_password():
    '''You need to write regex that will validate a password to make sure it meets the following

    criteria: At least six characters long
    contains a lowercase letter
    contains an uppercase letter
    contains a number
    Valid passwords will only be alphanumeric characters.
    '''
    print("задача 2_85:")
    passw = "123Qwer"
    regex = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])[A-Za-z0-9]{6,}$'
    result = re.match(regex, passw)
    if result:
        print("Пароль прошел проверку")
    else:
        print("Пароль  не прошел проверку")


def fizz_buzz():
    '''FizzBuzz Напишите программу, которая печатает цифры от 1 до 100, но вместо чисел,

    кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz,
    а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz
    '''
    print("задача 4_1:")
    numbers = list(range(1, 101))
    for i in numbers:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


def list_practice():
    '''List practice.Используйте генератор списков чтобы получить следующий:

    ['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
    Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
    Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
    Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
    Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента
    не было.
    '''
    print("задача 4_2:")
    pair_of_letters = [["a" + x for x in "bcd"] + ["b" + x for x in "bcd"]][0]
    pair_of_letters[::2]
    number_letters = [str(i) + "a" for i in range(1, 5)]
    number_letters.pop(1)
    print(number_letters)
    number_letters_copy = number_letters.copy()
    number_letters_copy.append("2a")


def tuple_practice():
    '''Tuple practice.

    Создайте кортеж из одного элемента, чтобы при итерировании по этому элементу последовательно
    выводились значения 1, 2, 3. Убедитесь что len() исходного кортежа возвращает 1.
    '''
    print("задача 4_3:")
    tuple1 = ([1, 2, 3], )
    for arr in tuple1:
        for item in arr:
            print(item)
    print("Длина исходного кортежа: ", len(tuple1))


def pairs_of_elements():
    '''Пары элементов. Дан список чисел. Посчитайте, сколько в нем пар элементов,

    равных друг другу.Считается, что любые два элемента, равные друг другу образуют
    одну пару, которую необходимо посчитать. Входные данные - строка из чисел,
    разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
    '''
    print("задача 4_4:")
    numbers = [int(s) for s in "1 1 1 1".split()]
    counter = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                counter += 1
    print("Количество пар: ", counter)


def unic_elements():
    '''Уникальные элементы в списке

    Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
    Элементы нужно выводить в том порядке, в котором они встречаются в списке.
    '''
    print("задача 4_5:")
    items = [int(s) for s in "1 2 4 2 5 1".split()]
    for i in items:
        if items.count(i) == 1:
            print("Уникальный элемент:", i)


def zero_left():
    '''Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,

    не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
    дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
    Распечатайте полученный список.
    '''
    print("задача 4_6:")
    items = [int(s) for s in "1 0 6 2 0 0 8".split()]
    for number in items:
        if number == 0:
            items.append(number)
            items.remove(number)
    print("Нули премещены влево:", items)


def dict_comprehensions():
    '''Dict comprehensions

    Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до 20,
    а значениями кубы этих чисел.
    '''
    print("задача 5_1:")
    dct = {int(element1 + 1): (element1 + 1) ** 3 for element1 in range(20)}
    print("Словарь, где ключ-числа от 1 до 20, значение-кубы этих чисел: ", dct)


def city_country():
    '''Города

    Дан список стран и городов каждой страны. Затем даны названия городов.
    Для каждого города укажите,
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


def union_of_sets():
    '''Даны два списка чисел. Посчитайте, сколько различных чисел

    содержится одновременно как в первом
    списке, так и во втором.
    '''
    print("задача 5_3:")
    first_list = "1 2 3 4 8 6".split()
    second_list = "4 5 6 7 9".split()
    print("В двух списках содержится ", len(set(first_list) | set(second_list)), " разных чисел")


def difference_of_sets():
    '''Даны два списка чисел. Посчитайте, сколько различных чисел входит

    только в один из этих списков
    '''
    print("задача 5_4:")
    first_list = "1 2 3 4 5".split()
    second_list = "4 5 6 7 8".split()
    print("Количество различных чисел: ", len(set(first_list) ^ set(second_list)))


def know_languages():
    '''Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все

    школьники и языки, которые знает хотя бы один из школьников.
    Входные данные
    Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi,
    после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
    Пример входных данных:
    3          # N количество школьников
    2          # M1 количество языков первого школьника
    Russian    # языки первого школьника
    English
    3          # M2 количество языков второго школьника
    Russian
    Belarusian
    English
    3
    Russian
    Italian
    French
    Выходные данные
    В первой строке выведите количество языков, которые знают все школьники.
    Начиная со второй строки
    - список таких языков. Затем - количество языков, которые знает хотя бы один школьник, на
    следующих строках - список таких языков.
    '''
    print("задача 5_5:")
    student1 = {'Russian', 'English'}
    student2 = {'Russian', 'Belarusian', 'English'}
    student3 = {'Russian', 'Italian', 'French'}
    known_by_everyone = set.intersection(student1, student2, student3)
    known_by_someone = set.union(student1, student2, student3)
    print("Знает каждый школьник: ", len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
    print("Знает из школьников:  ", len(known_by_someone), *sorted(known_by_someone), sep='\n')


def count_of_word():
    '''Во входной строке записан текст. Словом считается последовательность непробельных символов

    идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.
    Определите, сколько различных слов содержится в этом тексте.
    '''
    print("задача 5_6:")
    input_text = 'Во входной, строке !записан текст. Словом считается последовательность'
    without_symbols = re.sub(r'[;,.!?]', ' ', input_text)
    words = re.split(r'[\s]', without_symbols)
    count_words = 0
    for word in words:
        if word != "":
            count_words += 1
    print("В предложении ", count_words, " слов.")


def find_greatest_common_factor():
    '''Даны два натуральных числа. Вычислите их наибольший общий делитель при

    помощи алгоритма Евклида (мы не знаем функции и рекурсию).
    '''
    print("задача 5_7:")
    a = 1071
    b = 462
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print("Наибольший общий делитель чисел 1071 и 462 есть", a + b)
