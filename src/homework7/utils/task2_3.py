'''
Вводится строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
Например, если было введено "abc cde def", то должно быть выведено "abcdef".
'''


def remove_extra_symbols():
    print("задача 2_3:")
    string = "abc cde def"
    str_without_space = string.replace(' ', '')
    result = "".join(dict.fromkeys(str_without_space))
    print("Строка без пробелов и повторяющихся букв: " + result)
