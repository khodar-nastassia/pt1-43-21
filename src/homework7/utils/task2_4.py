'''
Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
Учитывать только английские буквы.
'''


import re


def count_upper_lowercase():
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
