# coding: utf-8

lst = ['Alex Ivanov', 'Ivan Petrov', 'Boris Britva', 'Monty Python', 'Alex Second']
num = int(input('Введите номер студента: '))
num -= 1

if num > len(lst) or num < 0:
    print('Нет такого студента!')
else:
    print (lst[num])


def my_func(a):
    return (int(input(a)))

numa = my_func('Введите начало среза студентов: ')
#int(input ('Введите начало среза студентов: '))
numb = my_func('Введите конец среза студентов: ')
#int(input ('Введите конец среза студентов: '))

if numa >= numb or numa < 0 or numb < 0:
    print('Некорректная выборка!')
else:
    print (lst[numa:numb])

    
lettercount = 0
letter = "P"

for i in lst:
    if letter in i:
        lettercount += 1 
s = 'Количество студентов с буквой "{}" в фамилии = {}' 
print (s.format(letter, lettercount))

names = []
students = []

for i in lst:
    name = i.split()[0]
    if name not in names:
        names.append(name)
        students.append([i])
    else:
        students[ names.index(name) ].append(i)
print(students)