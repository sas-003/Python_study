# coding: utf-8

import os
import math

#var def
mass = []
strnum = 0
file = '/Users/apple/Documents/list.txt'

#file creation
content = open(file, 'w')
for i in (1,2,3,4,5): #here u can change numbers
    content.write(str(i) + "\n")
content.close()

#file reading
nums = open(file)

for line in nums:
	mass.append(line)

#operations
summ = int(mass[0])+int(mass[1])
multsqrt = math.sqrt(int(mass[3])*int(mass[4]))
cos = (math.cos(int(mass[4])))

print ("Сумма [1] и [2] " + str(summ))
print ("Умножение и квадратный корень [3] и [4] " + str(multsqrt))
print ("Макс из 2ух результатов " + str(max(summ,multsqrt)))
print ("Косинус [5] " + str(cos))