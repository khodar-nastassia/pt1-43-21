'''
Найти самое длинное слово в введенном предложении.
Учтите что в предложении есть знаки препинания.
Подсказки:
- my_string.split([chars]) возвращает список строк.
- len(list) - количество элементов в списке
'''


import re


def main():
    string = input("Введите предложение ")
    max_word = ''
    for word in re.split(r'(s\+|,s\+)|(s\+|!|\.|\?)', string):
        if word:
            if len(word) > len(max_word):
                max_word = word


if __name__ == "__main__":
    main()
