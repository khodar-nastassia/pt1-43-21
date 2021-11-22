'''
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
'''

import re


def find_longest_word():
    print("задача 2_2:")
    input_text = "Учтите, что в предложении! есть знаки препинания."
    without_symbols = re.sub(r'[;,.!?]', '', input_text)
    print(without_symbols)
    words = without_symbols.split()
    print("Самое длинное слово: ", max(words, key=len))
