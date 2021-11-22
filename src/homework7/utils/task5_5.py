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


def know_languages():
    print("задача 5_5:")
    student1 = {'Russian', 'English'}
    student2 = {'Russian', 'Belarusian', 'English'}
    student3 = {'Russian', 'Italian', 'French'}
    known_by_everyone = set.intersection(student1, student2, student3)
    known_by_someone = set.union(student1, student2, student3)
    print("Знает каждый школьник: ", len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
    print("Знает из школьников:  ", len(known_by_someone), *sorted(known_by_someone), sep='\n')
