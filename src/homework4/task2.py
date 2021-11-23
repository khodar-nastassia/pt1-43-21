'''
List practice.Используйте генератор списков чтобы получить следующий:
['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
Используйте на предыдущий список slice чтобы получить следующий: ['ab', 'ad', 'bc'].
Используйте генератор списков чтобы получить следующий ['1a', '2a', '3a', '4a'].
Одной строкой удалите элемент  '2a' из прошлого списка и напечатайте его.
Скопируйте список и добавьте в него элемент '2a' так чтобы в исходном списке этого элемента
не было.
'''


def main():
    pair_of_letters = [["a" + x for x in "bcd"] + ["b" + x for x in "bcd"]][0]
    pair_of_letters[::2]
    number_letters = [str(i) + "a" for i in range(1, 5)]
    number_letters.pop(1)
    print(number_letters)
    number_letters_copy = number_letters.copy()
    number_letters_copy.append("2a")


if __name__ == "__main__":
    main()
