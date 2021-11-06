'''
Во входной строке записан текст. Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов или символами конца строки. Определите,
сколько различных слов содержится в этом тексте.
'''


import re


def main():
    inputText = 'Во входной, строке !записан текст. Словом считается последовательность'
    withoutSymbols = re.sub(r'[;,.!?]', ' ', inputText)
    words = re.split(r'[\s]', withoutSymbols)
    countWords = 0
    for word in words:
        if word != "":
            countWords += 1
    print(countWords)


if __name__ == "__main__":
    main()
