'''
Во входной строке записан текст. Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или символами конца строки. Определите,
сколько различных слов содержится в этом тексте.
'''


import re


def main():
    input_text = input("Введите предложение ")
    without_symbols = re.sub(r'[;,.!?]', ' ', input_text)
    words = re.split(r'[\s]', without_symbols)
    count_words = 0
    for word in words:
        if word != "":
            count_words += 1
    print("Количество слов в предложении:", count_words)


if __name__ == "__main__":
    main()
