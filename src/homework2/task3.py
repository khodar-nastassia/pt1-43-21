# Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было введено "abc cde def", то должно быть выведено "abcdef".
def main():
    string = input("Введите предложение ")
    strWithoutSpace = string.replace(' ', '')
    result = "".join(dict.fromkeys(strWithoutSpace))
    print(result)


if __name__ == "__main__":
    main()
