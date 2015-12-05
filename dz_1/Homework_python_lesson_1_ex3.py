# coding: utf-8

import os
import math

# PART I

D1 = 45
D2 = 338
D3 = 19

S1 = (math.pi * pow(D1,2)) / 4
S2 = (math.pi * pow(D2,2)) / 4
S3 = (math.pi * pow(D3,2)) / 4
Diff = (2 * max(S1,S2,S3) - S1 - S2 - S3)

print ("Первая площадь круга равна " + str(S1))
print ("Вторая площадь круга равна " + str(S2))
print ("Третья площадь круга равна " + str(S3))
print ("Вычитаем 2 площади из 3ей " + str(Diff) + "\n" + "\n")

# PART II

a = [1, -20, 38, 0, 44]
b = [88, -20, 48, 4, 33, 2]
i = 0
#p = 0

if len(a) - len(b) != 0: # Продолжаем список
    n = min(len(a), len(b))
    while n < max(len(a), len(b)):
        if len(a) > len(b):
            b += [a[n]] # Вместо несуществуещего элемента списка скопировали элемент из второго списка 
        else:
            a += [b[n]] # Вместо несуществуещего элемента списка скопировали элемент из второго списка 
        n += 1
    
while i < max(len(a), len(b)):
    #if a[i] exist:
        #a[i] = b[i]
    print ("Элементы " + str(a[i]) + " и " + str(b[i]) + ". Мин элемент №" + str(i) + " -> " + str(min (a[i], b[i])))
    if abs(a[i] - b[i]) < 15:
        print ("Поздравления на элементе " + str(i+1))
        #while p < abs(a[i] - b[i]) 
        # ....
        #p += 1
    i += 1
    
# PART III

X = input("Задай число X:")
Y = input("Задай число Y:")
Z = raw_input("Задай действие (+/-)")
summ = lambda x,y: x + y


if Z == '+':
    print ("Summ X, Y = " + summ(x,y)))
elif Z == '-':
    print ("Diff X, Y = " + str(int(X)-int(Y)))
else:
    print ("Unknown operation")