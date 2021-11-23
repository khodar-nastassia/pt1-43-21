'''
Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все
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
В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки
- список таких языков. Затем - количество языков, которые знает хотя бы один школьник, на
следующих строках - список таких языков.
'''


def main():
    count_of_students = int(input('Введите количество школьников : '))
    students_languages = []
    count1 = 0
    for i in range(count_of_students):
        count_of_languages = int(input('Введите количество языков i-ого школьника: '))
        languages = []
        student_languages = (languages)
        students_languages.append(student_languages)
        count1 += 1
        count2 = 0
        for k in range(count_of_languages):
            language = (input('Введите язык : '))
            languages.append(language)
            count2 += 1
    everyone = set(students_languages[0]) & set(students_languages[1]) & set(students_languages[2])
    someone = set(students_languages[0]) | set(students_languages[1]) | set(students_languages[2])
    print("Знает каждый школьник: " + str(len(everyone)), *sorted(everyone), sep='\n')
    print("Знает один из школьников: " + str(len(someone)), *sorted(someone), sep='\n')


if __name__ == "__main__":
    main()
